#include <iostream>

using namespace std;

int main()
{
	class Rect
	{
		int a, b;
		public:
			int get_a() {
				a = 0;
				return a;
			}
			int get_b_plus(int n) {
				return (b + n);
			}
	} rect;

	cout << rect.get_a() << " " << rect.get_b_plus(1) << endl;

	return 1;
}


