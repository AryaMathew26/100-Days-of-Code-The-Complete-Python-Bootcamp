alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = (int(input("Type the shift number:\n")))%26

should_continue=True
while should_continue:
  def caesar(init_text,shift_amount,cipher_direction):
    end_text=''
    for char in init_text:
      if char in alphabet:
        position=alphabet.index(char)
        if cipher_direction=='encode':
          end_text=end_text+alphabet[(position+shift)%26]
        else: 
          end_text=end_text+alphabet[position-shift]
      else:
        end_text+=char
    print(f"The {direction}d text is {end_text}")
  caesar(text,shift,direction)
  result=input("Type 'yes' if you want to go again. Type 'no otherwise'").lower()
  if result=='no':
    should_continue=False
    print("Goodbye")
