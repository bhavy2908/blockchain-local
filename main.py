from block import Block
import datetime

sender_name = "empty"
receiver_name = "empty"
amount = 0.00
datetime_object = 0
empty_string = sender_name + receiver_name + str(amount) + str(datetime_object)
initial_block = Block("0", empty_string)
datetime_object = datetime.datetime.now()
print("")
print("WELCOME! to the BlockChain Local Bank")
print("")
print("Time Stamp: ", datetime_object)
print("")
print("Transaction No. 1")
print("")
sender_name = input("Enter Sender's Name: ")
receiver_name = input("Enter Receiver's Name: ")
amount = input("Enter Amount: ")

transaction_sring = sender_name + " " + receiver_name + " " + \
    str(amount) + " " + str(datetime_object)
transaction_block = Block(initial_block.block_hash, transaction_sring)
print("-")
print("key : ", initial_block.block_hash)
print(sender_name, "sent", amount, "to", receiver_name, "on", datetime_object)
print("key : ", transaction_block.block_hash)
print("-")
i = 2


while True:
    print("Transaction No. ", i)
    print("")
    i += 1
    previous_block = transaction_block
    sender_name = input("Enter Sender's Name: ")
    receiver_name = input("Enter Receiver's Name: ")
    amount = input("Enter Amount: ")
    datetime_object = datetime.datetime.now()
    transaction_sring = sender_name + " " + receiver_name + " " + \
        str(amount) + " " + str(datetime_object)
    transaction_block = Block(previous_block.block_hash, transaction_sring)
    print("-")
    print("key : ", previous_block.block_hash)
    print(sender_name, "sent", amount, "to",
          receiver_name, "on", datetime_object)
    print("key : ", transaction_block.block_hash)
    print("-")
