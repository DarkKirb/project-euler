PYTHON := python
PYVERSION := $(shell $(PYTHON) -c "import sys; print(sys.version[:3])")

INCDIR := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc())")
PLATINCDIR := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc(plat_specific=True))")
LIBDIR1 := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
LIBDIR2 := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBPL'))")
PYLIB := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBRARY')[3:-2])")

CC := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('CC'))")
LINKCC := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LINKCC'))")
LINKFORSHARED := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LINKFORSHARED'))")
LIBS := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LIBS'))")
SYSLIBS :=  $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('SYSLIBS'))")

OUTS = _0001.eu _0002.eu _0003.eu _0004.eu _0005.eu _0006.eu _0007.eu _0008.eu _0009.eu _0010.eu _0011.eu _0012.eu _0013.eu _0014.eu _0015.eu _0016.eu _0017.eu
PYSRCS = $(addsuffix .py,$(basename $(OUTS)))
CSRCS = $(addsuffix .c,$(basename $(OUTS)))
OBJS = $(addsuffix .o,$(basename $(OUTS)))
all: $(OUTS)
%.eu: %.o
	$(LINKCC) -o $@ $^ -L$(LIBDIR1) -L$(LIBDIR2) -l$(PYLIB) $(LIBS) $(SYSLIBS) $(LINKFORSHARED)

%.o: %.c
	$(CC) -c $^ -I$(INCDIR) -I$(PLATINCDIR)

%.c: %.py
	$(PYTHON) -m cython --embed $^


clean:
	rm -f *~ *.o *.so core core* *.core *.c $(OUTS)
