import os

script_dir = os.path.dirname(__file__)
parameter_path = input("Enter filename: ")
abs_file_path = os.path.join(script_dir, parameter_path)

def park(slots, car_number):
      for i in range(len(slots)):
            if slots[i] == None:
                  print("Allocated slot number: " + str(i + 1))
                  slots[i] = car_number.replace('\n', '')
                  return slots
      print("Sorry, parking lot is full")
      return slots

def leave(slots, car_number, hours):
      for i in range(len(slots)):            
            if slots[i] == car_number:
                  slots[i] = None
                  charge = 10
                  hours -= 2                  
                  if hours > 0:
                        charge += hours * 10

                  print(f'Registraion number {car_number} with slot number {i + 1} is free with Charge ${charge}')
                  return slots
      print(f'Car with registration number {car_number} not found')
      return slots

def status(slots):
      print("Slot No. Registration No.")
      for s in range(len(slots)):
            if slots[s] != None:
                  print(str(s + 1) + " " + slots[s])


with open(abs_file_path, 'r') as f:
        #Handle parking slot creation
        parking_slot_number = int(f.readline().split(' ')[1])
        parking_slots = []
        for _ in range(parking_slot_number):
              parking_slots.append(None)
        
        for line in f:
            command = line.split(' ')[0].replace('\n', '')            
            if command == 'park':
                  car_number = line.split(' ')[1]
                  slot_number = park(parking_slots, car_number)                  
            elif command == 'leave':
                  car_number = line.split(' ')[1]
                  hours = line.split(' ')[2]
                  leave(parking_slots, car_number.replace('\n', ''), int(hours))
            elif command == 'status':                  
                  status(parking_slots)

