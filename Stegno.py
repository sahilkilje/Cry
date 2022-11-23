from stegano import lsb

message = input("Enter Message You want to hide: ")
img_file_text = lsb.hide('Sustainers HQ meet.png', message)

saved = 'sec.png'
img_file_text.save(saved)
print("Saved Succesfully")

message = lsb.reveal(saved)
print('Reveal message: ',str(message))
