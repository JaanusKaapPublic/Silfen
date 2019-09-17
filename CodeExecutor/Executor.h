#pragma once
#include "Conf.h"

typedef struct opAllocateData
{
	int varId;
	int varSize;
}opAllocateData;

typedef struct opPutBufferData
{
	int varId;
	int varOffset;
	int bufSize;
}opPutBufferData;

typedef struct opPutPointerData
{
	int varId;
	int varOffset;
	int ptrId;
}opPutPointerData;

typedef struct opNewVarPtrData
{
	int varId;
	int ptrId;
	int ptrOffset;
}opNewVarPtrData;

typedef struct opCopyData
{
	int varId;
	int varOffset;
	int srcId;
	int srcSize;
}opCopyData;

typedef struct opExecVarData
{
	int retVarId;
	int retVarSize;
	int paramCount;
}opExecVarData;

typedef char* (__stdcall *func0)();
typedef char* (__stdcall *func1)(char*);
typedef char* (__stdcall *func2)(char*, char*);
typedef char* (__stdcall *func3)(char*, char*, char*);
typedef char* (__stdcall *func4)(char*, char*, char*, char*);
typedef char* (__stdcall *func5)(char*, char*, char*, char*, char*);
typedef char* (__stdcall *func6)(char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func7)(char*, char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func8)(char*, char*, char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func9)(char*, char*, char*, char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func10)(char*, char*, char*, char*, char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func11)(char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func12)(char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func13)(char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func14)(char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func15)(char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*);
typedef char* (__stdcall *func16)(char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*, char*);

class Executor
{
private:
	char* variables[MAX_VARIABLES];
	FILE* calledFuncsLogFile;

	void opAllocate(FILE*);
	void opPutBuffer(FILE*);
	void opPutPointer(FILE*);
	void opNewVarPtr(FILE*);
	void opCopy(FILE*);
	void opExec(FILE*);
public:
	Executor();
	void run(char*);
	void setCalledFuncsLogFile(FILE*);
};