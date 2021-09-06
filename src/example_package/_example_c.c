#include "Python.h"
#include <stdlib.h>
#include <limits.h>

#define VERSION "1.0.0"


static PyObject*
return_ten(PyObject *module)
{
    return 10;
}

PyDoc_STRVAR(module_doc,
"example_package._example_c module.");

static PyMethodDef module_methods[] = {
    {"return_ten",
     (PyCFunction)return_ten, METH_NOARGS,
     PyDoc_STR("return_ten()")},
    {NULL, NULL}  /* sentinel */
};

#if PY_VERSION_HEX >= 0x03050000
static int
example_c_mod_exec(PyObject* module)
{
    PyObject *version;
    version = PyUnicode_FromString(VERSION);
    if (version == NULL)
        return -1;

    return PyModule_AddObject(module, "__version__", version);
}

static PyModuleDef_Slot _example_c_slots[] = {
    {Py_mod_exec, example_c_mod_exec},
    {0, NULL}
};
#endif

static struct PyModuleDef _example_c_module = {
    PyModuleDef_HEAD_INIT,
    "example_package._example_c",
    module_doc,
    0,
    module_methods,
#if PY_VERSION_HEX >= 0x03050000
    _example_c_slots,
#else
    NULL,
#endif
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC
PyInit__example_c(void)
{
#if PY_VERSION_HEX >= 0x03050000
    return PyModuleDef_Init(&_example_c_module);
#else
    PyObject *m, *version;

    m = PyModule_Create(&_example_c_module);
    if (m == NULL)
        return NULL;

    version = PyUnicode_FromString(VERSION);
    if (version == NULL)
        return NULL;

    PyModule_AddObject(m, "__version__", version);
    return m;
#endif
}
