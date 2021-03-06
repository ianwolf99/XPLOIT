#include <Windows.h>
#include <comdef.h>
#include <stdio.h>
#include <vector>
using namespace std;

#define CHUNK_SIZE 0x190
#define ALLOC_COUNT 10

class SomeObject {
public:
  void function1() {};
  virtual void virtual_function1() {};
};

int main(int args, char** argv) {
  int i;
  BSTR bstr;
  HANDLE hChunk;
  void* allocations[ALLOC_COUNT];
  BSTR bStrings[5];
  SomeObject* object = new SomeObject();
  HANDLE defaultHeap = GetProcessHeap();

  for (i = 0; i < ALLOC_COUNT; i++) {
    hChunk = HeapAlloc(defaultHeap, 0, CHUNK_SIZE);
    memset(hChunk, 'A', CHUNK_SIZE);
    allocations[i] = hChunk;
    printf("[%d] Heap chunk in backend : 0x%08x\n", i, hChunk);
  }

  HeapFree(defaultHeap, HEAP_NO_SERIALIZE, allocations[3]);

  for (i = 0; i < 5; i++) {
    bstr = SysAllocString(L"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
    bStrings[i] = bstr;
    printf("[%d] BSTR string : 0x%08x\n", i, bstr);
  }

  HeapFree(defaultHeap, HEAP_NO_SERIALIZE, allocations[4]);

  int objRef = (int) object;
  printf("SomeObject address for Chunk 3 : 0x%08x\n", objRef);
  vector<int> array1(40, objRef);
  vector<int> array2(40, objRef);
  vector<int> array3(40, objRef);
  vector<int> array4(40, objRef);
  vector<int> array5(40, objRef);
  vector<int> array6(40, objRef);
  vector<int> array7(40, objRef);
  vector<int> array8(40, objRef);
  vector<int> array9(40, objRef);
  vector<int> array10(40, objRef);

  system("PAUSE");
  return 0;
}