# memsim
memsim

A memory management system for heterogeneous memory systems

To run with an application:
  export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
  LD_PRELOAD=libhemem-[simple|lru|modified-lru].so <applicaiton>

