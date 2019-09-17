#include "stdafx.h"
#include <stdio.h>
#include <Windows.h>
#include "Executor.h"



Executor::Executor()
{
	calledFuncsLogFile = NULL;
	for (int x = 0; x < MAX_VARIABLES; x++)
	{
		variables[x] = (char*)0x0;
	}
}

void Executor::setCalledFuncsLogFile(FILE *f)
{
	calledFuncsLogFile = f;
}

void Executor::run(char* filename)
{
	FILE* f = fopen(filename, "rb");

	while (!feof(f))
	{
		char op =fgetc(f);
		if (op == 0x1)
			opAllocate(f);
		if (op == 0x2)
			opPutBuffer(f);
		if (op == 0x3)
			opPutPointer(f);
		if (op == 0x4)
			opNewVarPtr(f);
		if (op == 0x5)
			opCopy(f);
		if (op == 0x6)
			opExec(f);
	}
}

void Executor::opAllocate(FILE* f)
{
#ifdef _DEBUG
	printf("opAllocate\n");
#endif
	opAllocateData tmp;
	fread(&tmp, sizeof(opAllocateData), 1, f);
	variables[tmp.varId] = new char[tmp.varSize];
}

void Executor::opPutBuffer(FILE* f)
{
#ifdef _DEBUG
	printf("opPutBuffer\n");
#endif
	opPutBufferData tmp;
	fread(&tmp, sizeof(opPutBufferData), 1, f);
	fread(variables[tmp.varId] + tmp.varOffset, 1, tmp.bufSize, f);
}

void Executor::opPutPointer(FILE* f)
{
#ifdef _DEBUG
	printf("opPutPointer\n");
#endif
	opPutPointerData tmp;
	fread(&tmp, sizeof(opPutPointerData), 1, f);
	*((char**)(variables[tmp.varId] + tmp.varOffset)) = variables[tmp.ptrId];
}

void Executor::opNewVarPtr(FILE* f)
{
#ifdef _DEBUG
	printf("opNewVarPtr\n");
#endif
	opNewVarPtrData tmp;
	fread(&tmp, sizeof(opNewVarPtrData), 1, f);
	variables[tmp.varId] = variables[tmp.ptrId] + tmp.ptrOffset;
}

void Executor::opCopy(FILE* f)
{
#ifdef _DEBUG
	printf("opCopy\n");
#endif
	opCopyData tmp;
	fread(&tmp, sizeof(opCopyData), 1, f);
	memcpy(variables[tmp.varId] + tmp.varOffset, variables[tmp.srcId], tmp.srcSize);
}

void Executor::opExec(FILE* f)
{
#ifdef _DEBUG
	printf("opExec\n");
#endif
	opExecVarData tmp;
	tmp.retVarId = 0x11111111;
	tmp.retVarSize = 16;
	tmp.paramCount = 0x22222222;
	short len;
	char lib[1024];
	char func[1024];
	char* params[16];
	params[0] = (char*)0x1234567812345678;
	char* result;

	fread(&len, sizeof(short), 1, f);
	fread(lib, 1, len, f);
	lib[len] = 0;

	fread(&len, sizeof(short), 1, f);
	fread(func, 1, len, f);
	func[len] = 0;
	
	fread(&tmp, sizeof(tmp), 1, f);
	len = sizeof(tmp);


#ifdef _DEBUG
	printf("opExeclib: %s\n", lib);
#endif
	HINSTANCE hLib = LoadLibraryA(lib);
#ifdef _DEBUG
	printf("opExeclib: %s\n", func);
#endif
	void* funcPtr = (void*)GetProcAddress(hLib, func);

	for (int x = 0; x < tmp.paramCount; x++)
	{
		char type = fgetc(f);

		switch(type)
		{
			case 0:
				fread(&params[x], sizeof(char*), 1, f);
#ifdef _DEBUG
				printf("opExeclib-param-%d: <int> %Q\n", x, params[x]);
#endif
				break;
			case 1:
				int varId;
				fread(&varId, sizeof(int), 1, f);
#ifdef _DEBUG
				printf("opExeclib-param-%d: <var> %d\n", x, varId);
#endif
				params[x] = *((char**)(variables[varId]));
				break;
		}
	}

	if (calledFuncsLogFile)
	{
		fprintf(calledFuncsLogFile, "%s\n", func);
		fflush(calledFuncsLogFile);
	}
	try
	{
		switch (tmp.paramCount)
		{
		case 0:
			result = ((func0)funcPtr)();
			break;
		case 1:
			result = ((func1)funcPtr)(params[0]);
			break;
		case 2:
			result = ((func2)funcPtr)(params[0], params[1]);
			break;
		case 3:
			result = ((func3)funcPtr)(params[0], params[1], params[2]);
			break;
		case 4:
			result = ((func4)funcPtr)(params[0], params[1], params[2], params[3]);
			break;
		case 5:
			result = ((func5)funcPtr)(params[0], params[1], params[2], params[3], params[4]);
			break;
		case 6:
			result = ((func6)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5]);
			break;
		case 7:
			result = ((func7)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6]);
			break;
		case 8:
			result = ((func8)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7]);
			break;
		case 9:
			result = ((func9)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8]);
			break;
		case 10:
			result = ((func10)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9]);
			break;
		case 11:
			result = ((func11)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9], params[10]);
			break;
		case 12:
			result = ((func12)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9], params[10], params[11]);
			break;
		case 13:
			result = ((func13)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9], params[10], params[11], params[12]);
			break;
		case 14:
			result = ((func14)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9], params[10], params[11], params[12], params[13]);
			break;
		case 15:
			result = ((func15)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9], params[10], params[11], params[12], params[13], params[14]);
			break;
		case 16:
			result = ((func16)funcPtr)(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9], params[10], params[11], params[12], params[13], params[14], params[15]);
			break;
		}
	}
	catch (...)
	{
		printf("Esception happened\n");
	}
}