# def calculate_percentages(points):
#     a = int(input("Enter the number of points for A: "))
#     b = int(input("Enter the number of points for B: "))
#     c = int(input("Enter the number of points for C: "))
#     d = int(input("Enter the number of points for D: "))
#     f = int(input("Enter the number of points for F: "))
#     e = int(input("Enter the number of points for E: "))
#
#     total = sum([a, b, c, d, f, e])
#     percentages = [point / total * 100 for point in points]
#     return percentages
#
# company_points = [10, 20, 30, 40, 50, 60]
# percentages = calculate_percentages(company_points)
#
# for i, percentage in enumerate(percentages):
#     print(f"Company - {i+1}: {percentage:.2f}%")



# import random
#
# def story_generator():
#     # Step 1: Get user inputs
#     name = input("Enter a name: ")
#     place = input("Enter a place: ")
#     activity = input("Enter a favorite activity: ")
#     adjective = input("Enter an adjective (e.g., funny, mysterious): ")
#
#     # Step 2: Define story templates
#     stories = [
#         f"One day, {name} went to {place}. It was a {adjective} day, and {name} decided to spend it {activity}. Unexpectedly, something amazing happened!",
#         f"In the {adjective} town of {place}, {name} was well-known for {activity}. One day, {name} found a treasure map while enjoying their favorite activity!",
#         f"{name} always loved visiting {place}. On a particularly {adjective} afternoon, while {activity}, {name} discovered a secret door to another world.",
#         f"{place} was the last place anyone would call {adjective}, but for {name}, it was perfect for {activity}. What started as a simple day turned into an unforgettable adventure.",
#     ]
#
#     # Step 3: Randomly choose a story template
#     selected_story = random.choice(stories)
#
#     return selected_story
#
# # Step 4: Generate and display the story
# print("Welcome to the Random Story Generator!")
# result = story_generator()
# print("\nHere is your story:\n")
# print(result)

# pirveli_partia = int(input("pirveli partiis xmebi: "))
# meore_partia = int(input('meore partiis xmebi:'))
# mesame_partia = int(input('mesame partiis xmebi:'))
# meotxe_partia = int(input('meotxe partiis xmebi:'))
# mexute_partia = int(input('mexute partiis xmebi: '))
# meeqvse_partia = int(input('meeqvse partiis xmebi: '))
#
# archevnebi =[pirveli_partia,meore_partia,mesame_partia,meotxe_partia,mexute_partia,meeqvse_partia]
# jamuri_xmebi = sum(archevnebi)
#
# for i , partiebi in enumerate(archevnebi):
#     print(i,"xmebis raodenoba",round((partiebi / jamuri_xmebi) * 100, 2 ),'%')


# import random
#
# while True:
#     start_stop = str(input('do u want a story: [y/n]'))
#     if start_stop == 'y':
#         name = str(input('enter the name: '))
#         place = str(input('enter the place: '))
#         hobby = str(input('enter the hobby: '))
#         verb = str(input('enter the verb: '))
#         outcome1 = f"{name}ს საყვარელი საქმიანობაა {hobby} რასაც {place} ხშირად აკეთებს, ასევე უყვარს {verb}"
#         outcome2 = f"{name}ს ხშირად დადის {place}ში, სადაც ის {verb}."
#         outcome3 = f"{place}, {name}ს საყვარელი ადგილია.მისი ჰობია{hobby}"
#         outcome4 = f"{hobby}, საკმაოდ გავრცელებულია საქართველოში. {name} ერთ-ერთი მოყვარულთაგანია"
#         outcome5 = f"საქართველოში {name} გავრცელებულის სახელია. "
#         all_options = [outcome1,outcome2,outcome3,outcome4,outcome5]
#         print(random.choice(all_options))
#     elif start_stop == 'n':
#         print('bye')
#         break
#     else:
#         print('invalid input try y or n')








# from flask import Flask, jsonify
# from datetime import datetime
#
#
# app = Flask(__name__)
#
# @app.route('/greet', methods=['GET', 'POST'])
# def greet():
#     now = datetime.now()
#
#
#     return jsonify({
#         "message": "Hello, welcome to our API!",
#         "date": now.strftime("%Y-%m-%d %H:%M:%S")
#     })
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# @app.route('/convert/<string:unit>/<float:value>', methods=['GET'])
# def convert_temperature(unit, value):
#     if unit.upper() == 'C':
#         converted_value = value * 1.8 + 32
#         converted_unit = 'F'
#     elif unit.upper() == 'F':
#         converted_value = (value - 32) / 1.8
#         converted_unit = 'C'
#     else:
#         return jsonify({"error": "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit."}), 400
#
#     return jsonify({
#         "original_unit": unit.upper(),
#         "original_value": value,
#         "converted_unit": converted_unit,
#         "converted_value": round(converted_value, 2)
#     })
#
# @app.route('/')
# def home():
#     return "Welcome to the Temperature Converter API!"
#
# if __name__ == '__main__':
#     app.run(debug=True)
