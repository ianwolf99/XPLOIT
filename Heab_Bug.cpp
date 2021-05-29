#include <conio.h>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
using namespace std;
const bool printAddresses = true;
class Mutator {
protected:
int param;
public:
Mutator(int param) : param(param) {}
virtual int getParam() const {
return param;
}
virtual void mutate(void *data, int size) const = 0;
};
class Multiplier: public Mutator {
int reserved[40]; // not used, for now!
public:
Multiplier(int multiplier = 0) : Mutator(multiplier) {}
virtual void mutate(void *data, int size) const {
int *ptr = (int *)data;
for (int i = 0; i < size / 4; ++i)
ptr[i] *= getParam();
}
};
class LowerCaser : public Mutator {
public:
LowerCaser() : Mutator(0) {}
virtual void mutate(void *data, int size) const {
char *ptr = (char *)data;
for (int i = 0; i < size; ++i)
if (ptr[i] >= 'a' && ptr[i] <= 'z')
ptr[i] -= 0x20;
}
};
class Block {
void *data;
int size;
public:
Block(void *data, int size) : data(data), size(size) {}
void *getData() const { return data; }
int getSize() const { return size; }
};
// Global variables
vector<Block> blocks;
Mutator *mutators[] = { new Multiplier(2), new LowerCaser() };
void configureMutator() {
while (true) {
printf(
"1) Multiplier (multiplier = %d)\n"
"2) LowerCaser\n"
"3) Exit\n"
"\n"
"Your choice [1-3]: ", mutators[0]->getParam());
int choice = _getch();
printf("\n\n");
if (choice == '3')
break;
if (choice >= '1' && choice <= '3') {
if (choice == '1') {
if (printAddresses)
printf("mutators[0] = 0x%08x\n", mutators[0]);
delete mutators[0];
printf("multiplier (int): ");
int multiplier;
int res = scanf("%d", &multiplier);
fflush(stdin);
if (res) {
mutators[0] = new Multiplier(multiplier);
if (printAddresses)
printf("mutators[0] = 0x%08x\n", mutators[0]);
printf("Multiplier was configured\n\n");
}
	break;
}
else {
printf("LowerCaser is not configurable for now!\n\n");
}
}
else
printf("Wrong choice!\n");
}
} void listBlocks() {
printf("------- Blocks -------\n");
if (!printAddresses)
for (size_t i = 0; i < blocks.size(); ++i)
printf("block %d: size = %d\n", i, blocks[i].getSize());
else
for (size_t i = 0; i < blocks.size(); ++i)
printf("block %d: address = 0x%08x; size = %d\n", i, blocks[i].getData(), blocks[i].getSize());
printf("----------------------\n\n");
} void readBlock() {
char *data;
char filePath[1024];
while (true) {
printf("File path ('exit' to exit): ");
scanf("%s", filePath, sizeof(filePath));
fflush(stdin);
printf("\n");
if (!strcmp(filePath, "exit"))
return;
FILE *f = fopen(filePath, "rb");
if (!f)
printf("Can't open the file!\n\n");
else {
fseek(f, 0L, SEEK_END);
long bytes = ftell(f);
data = new char[bytes];
fseek(f, 0L, SEEK_SET);
int pos = 0;
while (pos < bytes) {
int len = bytes - pos > 200 ? 200 : bytes - pos;
fread(data + pos, 1, len, f);
pos += len;
}
fclose(f);
blocks.push_back(Block(data, bytes));
printf("Block read (%d bytes)\n\n", bytes);
break;
}
}
} 
void duplicateBlock() {
listBlocks();
while (true) {
printf("Index of block to duplicate (-1 to exit): ");
int index;
scanf("%d", &index);
fflush(stdin);
if (index == -1)
return;
if (index < 0 || index >= (int)blocks.size()) {
printf("Wrong index!\n");
}
else {
while (true) {
int copies;
printf("Number of copies (-1 to exit): ");
scanf("%d", &copies);
fflush(stdin);
if (copies == -1)
return;
if (copies <= 0)
printf("Wrong number of copies!\n");
else {
for (int i = 0; i < copies; ++i) {
int size = blocks[index].getSize();
void *data = new char[size];
memcpy(data, blocks[index].getData(), size);
blocks.push_back(Block(data, size));
}
return;
}
}
}
}
} 
void myExit() {
exit(0);
} 
void mutateBlock() {
listBlocks();
while (true) {
printf("Index of block to mutate (-1 to exit): ");
int index;
scanf("%d", &index);
fflush(stdin);
if (index == -1)
break;
if (index < 0 || index >= (int)blocks.size()) {
printf("Wrong index!\n");
}
else {
while (true) {
printf(
"1) Multiplier\n"
"2) LowerCaser\n"
"3) Exit\n"
"Your choice [1-3]: ");
int choice = _getch();
printf("\n\n");
if (choice == '3')
break;
if (choice >= '1' && choice <= '3') {
choice -= '0';
mutators[choice - 1]->mutate(blocks[index].getData(), blocks[index].getSize());
printf("The block was mutated.\n\n");
break;
}
else
printf("Wrong choice!\n\n");
}
break;
}
}
} 
int handleMenu() {
while (true) {
printf(
"1) Read block from file\n"
"2) List blocks\n"
"3) Duplicate Block\n"
"4) Configure mutator\n"
"5) Mutate block\n"
"6) Exit\n"
"\n"
"Your choice [1-6]: ");
int choice = _getch();
printf("\n\n");
if (choice >= '1' && choice <= '6')
return choice - '0';
else
printf("Wrong choice!\n\n");
}
} 
int main() {
typedef void(*funcPtr)();
funcPtr functions[] = { readBlock, listBlocks, duplicateBlock, configureMutator, mutateBlock, myExit };
while (true) {
int choice = handleMenu();
functions[choice - 1]();
} 
return 0;
}
