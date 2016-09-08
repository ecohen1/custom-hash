#include <iostream>
#include <string>

using namespace std;


struct Pair
{
    string value;
	string key;
    bool is_init;
};

class Hash
{
	public:
		int items;
		int space;
		Pair** values;
		
		Hash(int size);
		~Hash();
		bool set(string key, string value);
		string get(string key){ return ""; };
		string my_delete(string key){ return ""; };
		float load(){ return items/float(space); };
};
	
int main()
{
	Hash* hash = new Hash(2);

	bool success = hash->set("hi", "val1");
	cout << success << endl;
	
	bool another_success = hash->set("bye", "val2");
	cout << success << endl;
    
    string v1 = hash->values[0]->value;
    string v2 = hash->values[1]->value;
    cout << v1 << endl;
    cout << v2 << endl;

    // expects 1, 1, 1, 0, 1

	return 1;
}

Hash::Hash (int size)
{
	space = size;
	
	//values = (Pair**) malloc(sizeof(Pair*)*size);
    values = new Pair*[space];
	Pair pair;
	pair.is_init = false;
    for (int i=0;i<space;i++)
    {
        values[i] = &pair;    
    }
}

//Hash::~Hash()
//{
//	delete[] values;
//	free values[space];
//}

bool Hash::set (string key, string value)
{
	Pair* new_pair = new Pair();
    new_pair->value = value;
	new_pair->key = key;
	new_pair->is_init = true;
    for (int i=0; i<space; i++)
    {
		if (!(values[i]->is_init))
	    {
			values[i] = new_pair;
			return true;
		}
	}
	return false;
}
