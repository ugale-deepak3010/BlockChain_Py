import hashlib;         # if string is same then every time same hash code genereate. !

"""
NeuralCoinBlock is example of class.
t1 is transaction 1.

"""

class NeuralCoinBlock:
    def __init__(self, previous_block_hash , transaction_list ):
        self.previous_block_hash = previous_block_hash;
        self.transaction_list = transaction_list;

        self.block_data = " - ".join(transaction_list)    +    " - "+previous_block_hash ;

        self.block_hash = hashlib.sha256( self.block_data.encode() ).hexdigest(); # generate unique hex code.

t1 = "Deepak sends 2 NC to Lissa";
t2 = "Ram sends 4.1 NC to Deepak";
t3 = "Mike sends 3.2 NC to Bob";
t4 = "Danials sends 0.3 NC to Anna";
t5 = "Mike sends 1999999999 NC to Charlie";
t6 = "Mike sends 5.4 NC to Danials";

initial_block = NeuralCoinBlock("Initial String", [t1, t2] );
print(initial_block.block_data);
print(initial_block.block_hash);    
print("\n");

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4]);
print(second_block.block_data);
print(second_block.block_hash);
print("\n");

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6]);
print(third_block.block_data);
print(third_block.block_hash);
print("\n");






















print("");
    