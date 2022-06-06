#include <Python.h>

/**
* print_python_list_info - prints info about python list
* @p: a PyObject list
*/

void print_python_list_info(PyObject *p)
{
	int lsize, j, alloc;
	PyObject *ptr;
	
	lsize = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	
	printf("[*] Size of the Python List = %d\n", lsize);
	printf("[*] Allocated = %d\n", alloc);

	for (j = 0; lsize > j; j++)
	{
		printf("Element %d: ", j);
		ptr = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(ptr)->tp_name);
	}
}
