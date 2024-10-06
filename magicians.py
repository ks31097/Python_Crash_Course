magicians = ['alice', 'david', 'carolina']
for magician in sorted(magicians, reverse=True):
# for magician in magicians:
    magician = magician.title()
    
    great_message = f"{magician}, that was a great trick!"
    print(great_message)
    
    wait_message = f"I can't wait to see your next trick, {magician}.\n"
    print(wait_message)

print("Thank you, everyone. That was a great magic show!")