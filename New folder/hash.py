class HashTable:
    def __init__(self):
        self.collection={}
    def hash(self,string):
        total=0
        for char in string:
            total+=ord(char)# ord() function returns the unicode code point for a given character
        return total        
    def add(self,key,value):
        hash_value=self.hash(key)# compute the hash value for the given key
        if hash_value not in self.collection:#check if the hash value alreadyexists int the collection
            self.collection[hash_value]={}#if the hash value does not exist,create a new dictionary at the hash value

        self.collection[hash_value][key]=value #add the key value pair to the dictionary at the hash value and it also handles collision s   
    def remove(self,key):
        hash_value=self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:#check if the hash value exists in the collections and key exists in the dictionary at the hash value.
            del self.collection[hash_value][key]#renove the key value pair from dictionary at the hash value
            if not self.collection[hash_value]:#use the not operator to check if the dictionary at the hash value is empty after removing the key-value
               del self.collection[hash_value]#remove hash value from the collection

       # if not self.collection[hash_value]:
           # del self.collection[hash_value]
    def lookup(self,key):
        hash_value=self.hash(key)
        if hash_value in self.collection and key in self.collection[hash_value]:
           return self.collection[hash_value][key]#it return the value of th key in that hash value
        return None 


