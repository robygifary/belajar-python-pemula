# Belajar default argument value

def say_hello(first_name = "Robby", last_name = ""):
  print(f"Hello {first_name} - {last_name}")

say_hello("Beny")
say_hello(last_name="Jhon")