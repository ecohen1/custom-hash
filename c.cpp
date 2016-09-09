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
		string get(string key);
		string Delete(string key);
		float load(){ return items/float(space); };
};
	
int main()
{
	Hash* hash = new Hash(2);

	bool success = hash->set("hi", "val1");
	cout << success << endl;
	
	bool another_success = hash->set("bye", "val2");
	cout << another_success << endl;
    
	bool failure = hash->set("none", "val3");
	cout << failure << endl;
	
	cout << hash->get("hi") << endl;
	cout << hash->get("bye") << endl;

	string del_value = hash->Delete("hi");
	cout << del_value << endl;
	cout << hash->get("bye") << endl;
	cout << hash->get("hi") << endl;
	
	// expects 1, 1, 0, val1, val2, val1, val2, NULL (0)

	return 1;
}

Hash::Hash (int size)
{
	space = size;
	
	values = new Pair*[space];
	Pair pair;
	pair.is_init = false;
	for (int i=0;i<space;i++)
	{
        	values[i] = &pair;    
    	}
}

Hash::~Hash()
{
	delete[] values;
}

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

string Hash::get (string key)
{
	for (int i=0; i<space; i++)
	{
		if (values[i]->is_init && values[i]->key == key)
		{
			return values[i]->value;
		}
	}
	return (string) "";
}

string Hash::Delete (string key)
{
	Pair empty_pair;
	empty_pair.is_init = false;

	for (int i=0; i<space; i++)
	{
		if (values[i]->is_init && values[i]->key == key)
		{
			string value = values[i]->value;
			*values[i] = empty_pair;
			return value;
		}
	}
}
