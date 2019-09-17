Data = {
	'NtAccessCheck': {'code': 0x0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'pSecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientToken', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'GenericMapping', 'type':'PGENERIC_MAPPING', 'in': True, 'out': False, 'optional': False},
			{'name': 'PrivilegeSet', 'type':'PPRIVILEGE_SET', 'in': False, 'out': True, 'optional': True},
			{'name': 'PrivilegeSetLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'GrantedAccess', 'type':'PACCESS_MASK', 'in': False, 'out': True, 'optional': False},
			{'name': 'AccessStatus', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': False},
		]},

	'NtWorkerFactoryWorkerReady': {'code': 0x1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'WorkerFactoryHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAcceptConnectPort': {'code': 0x2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ServerPortHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'AlternativeReceivePortHandle', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'ConnectionReply', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'AcceptConnection', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'ServerSharedMemory', 'type':'PPORT_SECTION_WRITE', 'in': True, 'out': True, 'optional': True},
			{'name': 'ClientSharedMemory', 'type':'PPORT_SECTION_READ', 'in': False, 'out': True, 'optional': True},
		]},

	'NtMapUserPhysicalPagesScatter': {'code': 0x3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'VirtualAddresses', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfPages', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'UserPfnArray', 'type':'PULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtWaitForSingleObject': {'code': 0x4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCallbackReturn': {'code': 0x5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'OutputBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'OutputLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Status', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReadFile': {'code': 0x6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ByteOffset', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'Key', 'type':'PULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtDeviceIoControlFile': {'code': 0x7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'IoControlCode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'InputBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'InputBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'OutputBuffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'OutputBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtWriteFile': {'code': 0x8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ByteOffset', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'Key', 'type':'PULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtRemoveIoCompletion': {'code': 0x9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'IoCompletionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyContext', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'ApcContext', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtReleaseSemaphore': {'code': 0xA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SemaphoreHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReleaseCount', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousCount', 'type':'PLONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtReplyWaitReceivePort': {'code': 0xB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortContext', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'ReplyMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ReceiveMessage', 'type':'PPORT_MESSAGE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtReplyPort': {'code': 0xC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReplyMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationThread': {'code': 0xD, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformationClass', 'type':'THREADINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetEvent': {'code': 0xE, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousState', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtClose': {'code': 0xF, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Handle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueryObject': {'code': 0x10, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Handle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectInformationClass', 'type':'OBJECT_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'ObjectInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryInformationFile': {'code': 0x11, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'FileInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileInformationClass', 'type':'FILE_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenKey': {'code': 0x12, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtEnumerateValueKey': {'code': 0x13, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Index', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyValueInformationClass', 'type':'KEY_VALUE_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyValueInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResultLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtFindAtom': {'code': 0x14, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'AtomName', 'type':'PWSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Atom', 'type':'PUSHORT', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryDefaultLocale': {'code': 0x15, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'UserProfile', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'DefaultLocaleId', 'type':'PLCID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryKey': {'code': 0x16, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyInformationClass', 'type':'KEY_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResultLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryValueKey': {'code': 0x17, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ValueName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyValueInformationClass', 'type':'KEY_VALUE_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyValueInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResultLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtAllocateVirtualMemory': {'code': 0x18, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
			{'name': 'ZeroBits', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'RegionSize', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'AllocationType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Protect', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueryInformationProcess': {'code': 0x19, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProcessInformationClass', 'type':'PROCESSINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProcessInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'ProcessInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	#TODO: Unknown parameter types
	'NtWaitForMultipleObjects32': {'code': 0x1A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtWriteFileGather': {'code': 0x1B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'SegmentArray', 'type':'PFILE_SEGMENT_ELEMENT', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ByteOffset', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Key', 'type':'PULONG', 'in': True, 'out': False, 'optional': True},
		]},

	#'NtSetInformationProcess': {'code': 0x1C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
	#	[
	#		{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
	#		{'name': 'ProcessInformationClass', 'type':'PROCESSINFOCLASS', 'in': True, 'out': False, 'optional': False},
	#		{'name': 'ProcessInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
	#		{'name': 'ProcessInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
	#	]},

	'NtCreateKey': {'code': 0x1D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'TitleIndex', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Class', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Disposition', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtFreeVirtualMemory': {'code': 0x1E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
			{'name': 'RegionSize', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'FreeType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtImpersonateClientOfPort': {'code': 0x1F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Message', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReleaseMutant': {'code': 0x20, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'MutantHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousCount', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryInformationToken': {'code': 0x21, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenInformationClass', 'type':'TOKEN_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'TokenInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtRequestWaitReplyPort': {'code': 0x22, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'RequestMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReplyMessage', 'type':'PPORT_MESSAGE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryVirtualMemory': {'code': 0x23, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'MemoryInformationClass', 'type':'MEMORY_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'MemoryInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'MemoryInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtOpenThreadToken': {'code': 0x24, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'OpenAsSelf', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryInformationThread': {'code': 0x25, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformationClass', 'type':'THREADINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'ThreadInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtOpenProcess': {'code': 0x26, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientId', 'type':'PCLIENT_ID', 'in': True, 'out': False, 'optional': True},
		]},

	'NtSetInformationFile': {'code': 0x27, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'FileInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileInformationClass', 'type':'FILE_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtMapViewOfSection': {'code': 0x28, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SectionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
			{'name': 'ZeroBits', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'CommitSize', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': False},
			{'name': 'SectionOffset', 'type':'PLARGE_INTEGER', 'in': True, 'out': True, 'optional': True},
			{'name': 'ViewSize', 'type':'PSIZE_T', 'in': True, 'out': True, 'optional': False},
			{'name': 'InheritDisposition', 'type':'SECTION_INHERIT', 'in': True, 'out': False, 'optional': False},
			{'name': 'AllocationType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Win32Protect', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAccessCheckAndAuditAlarm': {'code': 0x29, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SubsystemName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleId', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ObjectTypeName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'GenericMapping', 'type':'PGENERIC_MAPPING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectCreation', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'GrantedAccess', 'type':'PACCESS_MASK', 'in': False, 'out': True, 'optional': False},
			{'name': 'AccessStatus', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': False},
			{'name': 'GenerateOnClose', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': False},
		]},

	'NtUnmapViewOfSection': {'code': 0x2A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReplyWaitReceivePortEx': {'code': 0x2B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortContext', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'ReplyMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ReceiveMessage', 'type':'PPORT_MESSAGE', 'in': False, 'out': True, 'optional': False},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtTerminateProcess': {'code': 0x2C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ExitStatus', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetEventBoostPriority': {'code': 0x2D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReadFileScatter': {'code': 0x2E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'SegmentArray', 'type':'PFILE_SEGMENT_ELEMENT', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ByteOffset', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'Key', 'type':'PULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtOpenThreadTokenEx': {'code': 0x2F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'OpenAsSelf', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleAttributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtOpenProcessTokenEx': {'code': 0x30, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleAttributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryPerformanceCounter': {'code': 0x31, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PerformanceCounter', 'type':'PLARGE_INTEGER', 'in': False, 'out': True, 'optional': False},
			{'name': 'PerformanceFrequency', 'type':'PLARGE_INTEGER', 'in': False, 'out': True, 'optional': True},
		]},

	'NtEnumerateKey': {'code': 0x32, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Index', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyInformationClass', 'type':'KEY_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResultLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtOpenFile': {'code': 0x33, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'ShareAccess', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'OpenOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDelayExecution': {'code': 0x34, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Alertable', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'DelayInterval', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueryDirectoryFile': {'code': 0x35, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'FileInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileInformationClass', 'type':'FILE_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnSingleEntry', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'RestartScan', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQuerySystemInformation': {'code': 0x36, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SystemInformationClass', 'type':'SYSTEM_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'SystemInformation', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
			{'name': 'SystemInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtOpenSection': {'code': 0x37, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SectionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueryTimer': {'code': 0x38, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TimerInformationClass', 'type':'TIMER_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'TimerInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'TimerInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtFsControlFile': {'code': 0x39, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'FsControlCode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'InputBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'InputBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'OutputBuffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'OutputBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtWriteVirtualMemory': {'code': 0x3A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfBytesToWrite', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfBytesWritten', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtCloseObjectAuditAlarm': {'code': 0x3B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SubsystemName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleId', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'GenerateOnClose', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDuplicateObject': {'code': 0x3C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SourceProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SourceHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TargetProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'TargetHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': True},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleAttributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Options', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueryAttributesFile': {'code': 0x3D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileInformation', 'type':'PFILE_BASIC_INFORMATION', 'in': False, 'out': True, 'optional': False},
		]},

	'NtClearEvent': {'code': 0x3E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReadVirtualMemory': {'code': 0x3F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'BufferSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfBytesRead', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtOpenEvent': {'code': 0x40, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAdjustPrivilegesToken': {'code': 0x41, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DisableAllPrivileges', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewState', 'type':'PTOKEN_PRIVILEGES', 'in': True, 'out': False, 'optional': True},
			{'name': 'BufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousState', 'type':'PTOKEN_PRIVILEGES', 'in': False, 'out': True, 'optional': True},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtDuplicateToken': {'code': 0x42, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ExistingTokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'EffectiveOnly', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenType', 'type':'TOKEN_TYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewTokenHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtContinue': {'code': 0x43, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ContextRecord', 'type':'PCONTEXT', 'in': True, 'out': False, 'optional': False},
			{'name': 'TestAlert', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueryDefaultUILanguage': {'code': 0x44, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DefaultUILanguageId', 'type':'PLANGID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueueApcThread': {'code': 0x45, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ApcRoutine', 'type':'PKNORMAL_ROUTINE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ApcArgument1', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcArgument2', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcArgument3', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
		]},

	'NtYieldExecution': {'code': 0x46, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtAddAtom': {'code': 0x47, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'AtomName', 'type':'PWSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Atom', 'type':'PUSHORT', 'in': False, 'out': True, 'optional': True},
		]},

	'NtCreateEvent': {'code': 0x48, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'EventType', 'type':'EVENT_TYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'InitialState', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueryVolumeInformationFile': {'code': 0x49, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'FsInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'FsInformationClass', 'type':'FS_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateSection': {'code': 0x4A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SectionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'MaximumSize', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'SectionPageProtection', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'AllocationAttributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtFlushBuffersFile': {'code': 0x4B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
		]},

	'NtApphelpCacheControl': {'code': 0x4C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Service', 'type':'APPHELPCACHESERVICECLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ServiceData', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateProcessEx': {'code': 0x4D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'ParentProcess', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SectionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'DebugPort', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ExceptionPort', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'JobMemberLevel', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateThread': {'code': 0x4E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientId', 'type':'PCLIENT_ID', 'in': False, 'out': True, 'optional': False},
			{'name': 'ThreadContext', 'type':'PCONTEXT', 'in': True, 'out': False, 'optional': False},
			{'name': 'InitialTeb', 'type':'PUSER_STACK', 'in': True, 'out': False, 'optional': False},
			{'name': 'CreateSuspended', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtIsProcessInJob': {'code': 0x4F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'JobHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtProtectVirtualMemory': {'code': 0x50, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
			{'name': 'RegionSize', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'NewProtect', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'OldProtect', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQuerySection': {'code': 0x51, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SectionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SectionInformationClass', 'type':'SECTION_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'SectionInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'SectionInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtResumeThread': {'code': 0x52, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousSuspendCount', 'type':'PULONG', 'in': True, 'out': True, 'optional': True},
		]},

	'NtTerminateThread': {'code': 0x53, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ExitStatus', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReadRequestData': {'code': 0x54, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Message', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DataEntryIndex', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'BufferSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfBytesRead', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtCreateFile': {'code': 0x55, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'AllocationSize', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'FileAttributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ShareAccess', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'CreateDisposition', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'EaBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'EaLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueryEvent': {'code': 0x56, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'EventInformationClass', 'type':'EVENT_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'EventInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'EventInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtWriteRequestData': {'code': 0x57, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Request', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DataIndex', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResultLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtOpenDirectoryObject': {'code': 0x58, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DirectoryHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAccessCheckByTypeAndAuditAlarm': {'code': 0x59, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SubsystemName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleId', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ObjectTypeName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'PrincipalSelfSid', 'type':'PSID', 'in': True, 'out': False, 'optional': True},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'AuditType', 'type':'AUDIT_EVENT_TYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectTypeList', 'type':'POBJECT_TYPE_LIST', 'in': True, 'out': False, 'optional': True},
			{'name': 'ObjectTypeListLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'GenericMapping', 'type':'PGENERIC_MAPPING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectCreation', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'GrantedAccess', 'type':'PACCESS_MASK', 'in': False, 'out': True, 'optional': False},
			{'name': 'AccessStatus', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'GenerateOnClose', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': False},
		]},

	'NtWaitForMultipleObjects': {'code': 0x5B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PHANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'WAIT_TYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationObject': {'code': 0x5C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Handle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectInformationClass', 'type':'OBJECT_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCancelIoFile': {'code': 0x5D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
		]},

	'NtTraceEvent': {'code': 0x5E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TraceHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'FieldSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Fields', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtPowerInformation': {'code': 0x5F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'InformationLevel', 'type':'POWER_INFORMATION_LEVEL', 'in': True, 'out': False, 'optional': False},
			{'name': 'InputBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'InputBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'OutputBuffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'OutputBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetValueKey': {'code': 0x60, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ValueName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'TitleIndex', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'Type', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SystemData', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'DataSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCancelTimer': {'code': 0x61, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'CurrentState', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': True},
		]},

	'NtSetTimer': {'code': 0x62, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DueTime', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'TimerApcRoutine', 'type':'PTIMER_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'TimerContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ResumeTimer', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'Period', 'type':'LONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'PreviousState', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': True},
		]},

	'NtAccessCheckByType': {'code': 0x63, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'PrincipalSelfSid', 'type':'PSID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ClientToken', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectTypeList', 'type':'POBJECT_TYPE_LIST', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectTypeListLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'GenericMapping', 'type':'PGENERIC_MAPPING', 'in': True, 'out': False, 'optional': False},
			{'name': 'PrivilegeSet', 'type':'PPRIVILEGE_SET', 'in': False, 'out': True, 'optional': False},
			{'name': 'PrivilegeSetLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'GrantedAccess', 'type':'PACCESS_MASK', 'in': False, 'out': True, 'optional': False},
			{'name': 'AccessStatus', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtAccessCheckByTypeResultList': {'code': 0x64, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'PrincipalSelfSid', 'type':'PSID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ClientToken', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectTypeList', 'type':'POBJECT_TYPE_LIST', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectTypeListLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'GenericMapping', 'type':'PGENERIC_MAPPING', 'in': True, 'out': False, 'optional': False},
			{'name': 'PrivilegeSet', 'type':'PPRIVILEGE_SET', 'in': False, 'out': True, 'optional': False},
			{'name': 'PrivilegeSetLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'GrantedAccess', 'type':'PACCESS_MASK', 'in': False, 'out': True, 'optional': False},
			{'name': 'AccessStatus', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtAccessCheckByTypeResultListAndAuditAlarm': {'code': 0x65, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SubsystemName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleId', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ObjectTypeName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'PrincipalSelfSid', 'type':'PSID', 'in': True, 'out': False, 'optional': True},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'AuditType', 'type':'AUDIT_EVENT_TYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectTypeList', 'type':'POBJECT_TYPE_LIST', 'in': True, 'out': False, 'optional': True},
			{'name': 'ObjectTypeListLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'GenericMapping', 'type':'PGENERIC_MAPPING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectCreation', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'GrantedAccess', 'type':'PACCESS_MASK', 'in': False, 'out': True, 'optional': False},
			{'name': 'AccessStatus', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'GenerateOnClose', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtAccessCheckByTypeResultListAndAuditAlarmByHandle': {'code': 0x66, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SubsystemName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleId', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ClientToken', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectTypeName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'PrincipalSelfSid', 'type':'PSID', 'in': True, 'out': False, 'optional': True},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'AuditType', 'type':'AUDIT_EVENT_TYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectTypeList', 'type':'POBJECT_TYPE_LIST', 'in': True, 'out': False, 'optional': True},
			{'name': 'ObjectTypeListLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'GenericMapping', 'type':'PGENERIC_MAPPING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectCreation', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'GrantedAccess', 'type':'PACCESS_MASK', 'in': False, 'out': True, 'optional': False},
			{'name': 'AccessStatus', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'GenerateOnClose', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtAcquireProcessActivityReference': {'code': 0x67, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtAddAtomEx': {'code': 0x68, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'AtomName', 'type':'PWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Atom', 'type':'PRTL_ATOM', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAddBootEntry': {'code': 0x69, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'BootEntry', 'type':'PBOOT_ENTRY', 'in': True, 'out': False, 'optional': False},
			{'name': 'Id', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtAddDriverEntry': {'code': 0x6A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DriverEntry', 'type':'PEFI_DRIVER_ENTRY', 'in': True, 'out': False, 'optional': False},
			{'name': 'Id', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtAdjustGroupsToken': {'code': 0x6B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResetToDefault', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewState', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': True},
			{'name': 'BufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'PreviousState', 'type':'PTOKEN_GROUPS', 'in': False, 'out': True, 'optional': True},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtAdjustTokenClaimsAndDeviceGroups': {'code': 0x6C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'UserResetToDefault', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'DeviceResetToDefault', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'DeviceGroupsResetToDefault', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewUserState', 'type':'PTOKEN_SECURITY_ATTRIBUTES_INFORMATION', 'in': True, 'out': False, 'optional': True},
			{'name': 'NewDeviceState', 'type':'PTOKEN_SECURITY_ATTRIBUTES_INFORMATION', 'in': True, 'out': False, 'optional': True},
			{'name': 'NewDeviceGroupsState', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': True},
			{'name': 'UserBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousUserState', 'type':'PTOKEN_SECURITY_ATTRIBUTES_INFORMATION', 'in': False, 'out': True, 'optional': True},
			{'name': 'DeviceBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousDeviceState', 'type':'PTOKEN_SECURITY_ATTRIBUTES_INFORMATION', 'in': False, 'out': True, 'optional': True},
			{'name': 'DeviceGroupsBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousDeviceGroups', 'type':'PTOKEN_GROUPS', 'in': False, 'out': True, 'optional': True},
			{'name': 'UserReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'DeviceReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'DeviceGroupsReturnBufferLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtAlertResumeThread': {'code': 0x6D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousSuspendCount', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtAlertThread': {'code': 0x6E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtAlertThreadByThreadId': {'code': 0x6F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAllocateLocallyUniqueId': {'code': 0x70, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Luid', 'type':'PLUID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtAllocateReserveObject': {'code': 0x71, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'MemoryReserveHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'Type', 'type':'MEMORY_RESERVE_TYPE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAllocateUserPhysicalPages': {'code': 0x72, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfPages', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'UserPfnArray', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtAllocateUuids': {'code': 0x73, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Time', 'type':'PLARGE_INTEGER', 'in': False, 'out': True, 'optional': False},
			{'name': 'Range', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'Sequence', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'Seed', 'type':'PUCHAR', 'in': False, 'out': True, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtAllocateVirtualMemoryEx': {'code': 0x74, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtAlpcAcceptConnectPort': {'code': 0x75, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ConnectionPortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'PortAttributes', 'type':'PALPC_PORT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'PortContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ConnectionRequest', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ConnectionMessageAttributes', 'type':'PALPC_MESSAGE_ATTRIBUTES', 'in': True, 'out': True, 'optional': True},
			{'name': 'AcceptConnection', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcCancelMessage': {'code': 0x76, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MessageContext', 'type':'PALPC_CONTEXT_ATTR', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcConnectPort': {'code': 0x77, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'PortName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'PortAttributes', 'type':'PALPC_PORT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'RequiredServerSid', 'type':'PSID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ConnectionMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': True, 'optional': True},
			{'name': 'BufferLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': True},
			{'name': 'OutMessageAttributes', 'type':'PALPC_MESSAGE_ATTRIBUTES', 'in': True, 'out': True, 'optional': True},
			{'name': 'InMessageAttributes', 'type':'PALPC_MESSAGE_ATTRIBUTES', 'in': True, 'out': True, 'optional': True},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtAlpcConnectPortEx': {'code': 0x78, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ConnectionPortObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientPortObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'PortAttributes', 'type':'PALPC_PORT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ServerSecurityRequirements', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': True},
			{'name': 'ConnectionMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': True, 'optional': True},
			{'name': 'BufferLength', 'type':'PSIZE_T', 'in': True, 'out': True, 'optional': True},
			{'name': 'OutMessageAttributes', 'type':'PALPC_MESSAGE_ATTRIBUTES', 'in': True, 'out': True, 'optional': True},
			{'name': 'InMessageAttributes', 'type':'PALPC_MESSAGE_ATTRIBUTES', 'in': True, 'out': True, 'optional': True},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtAlpcCreatePort': {'code': 0x79, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'PortAttributes', 'type':'PALPC_PORT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
		]},

	'NtAlpcCreatePortSection': {'code': 0x7A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SectionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'SectionSize', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': False},
			{'name': 'AlpcSectionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ActualSectionSize', 'type':'PSIZE_T', 'in': False, 'out': True, 'optional': False},
		]},

	'NtAlpcCreateResourceReserve': {'code': 0x7B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MessageSize', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceId', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtAlpcCreateSectionView': {'code': 0x7C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ViewAttributes', 'type':'PALPC_DATA_VIEW_ATTR', 'in': True, 'out': True, 'optional': False},
		]},

	'NtAlpcCreateSecurityContext': {'code': 0x7D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityAttribute', 'type':'PALPC_SECURITY_ATTR', 'in': True, 'out': True, 'optional': False},
		]},

	'NtAlpcDeletePortSection': {'code': 0x7E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SectionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcDeleteResourceReserve': {'code': 0x7F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceId', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcDeleteSectionView': {'code': 0x80, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ViewBase', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcDeleteSecurityContext': {'code': 0x81, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ContextHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcDisconnectPort': {'code': 0x82, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcImpersonateClientContainerOfPort': {'code': 0x83, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Message', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcImpersonateClientOfPort': {'code': 0x84, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Message', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcOpenSenderProcess': {'code': 0x85, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcOpenSenderThread': {'code': 0x86, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcQueryInformation': {'code': 0x87, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'PortInformationClass', 'type':'ALPC_PORT_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortInformation', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtAlpcQueryInformationMessage': {'code': 0x88, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
			{'name': 'MessageInformationClass', 'type':'ALPC_MESSAGE_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'MessageInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtAlpcRevokeSecurityContext': {'code': 0x89, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ContextHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAlpcSendWaitReceivePort': {'code': 0x8A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SendMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': True},
			{'name': 'SendMessageAttributes', 'type':'PALPC_MESSAGE_ATTRIBUTES', 'in': True, 'out': True, 'optional': True},
			{'name': 'ReceiveMessage', 'type':'PPORT_MESSAGE', 'in': False, 'out': True, 'optional': True},
			{'name': 'BufferLength', 'type':'PSIZE_T', 'in': True, 'out': True, 'optional': True},
			{'name': 'ReceiveMessageAttributes', 'type':'PALPC_MESSAGE_ATTRIBUTES', 'in': True, 'out': True, 'optional': True},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtAlpcSetInformation': {'code': 0x8B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortInformationClass', 'type':'ALPC_PORT_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAreMappedFilesTheSame': {'code': 0x8C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'File1MappedAsAnImage', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'File2MappedAsFile', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAssignProcessToJobObject': {'code': 0x8D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'JobHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtAssociateWaitCompletionPacket': {'code': 0x8E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'WaitCompletionPacketHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoCompletionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TargetObjectHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatus', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusInformation', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'AlreadySignaled', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': True},
		]},

	#TODO: Unknown function until now
	'NtCallEnclave': {'code': 0x8F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtCancelIoFileEx': {'code': 0x90, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoRequestToCancel', 'type':'PIO_STATUS_BLOCK', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
		]},

	'NtCancelSynchronousIoFile': {'code': 0x91, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoRequestToCancel', 'type':'PIO_STATUS_BLOCK', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
		]},

	'NtCancelTimer2': {'code': 0x92, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Parameters', 'type':'PT2_CANCEL_PARAMETERS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCancelWaitCompletionPacket': {'code': 0x93, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'WaitCompletionPacketHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'RemoveSignaledPacket', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCommitComplete': {'code': 0x94, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCommitEnlistment': {'code': 0x95, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	#TODO: Unknown parameter types
	'NtCommitRegistryTransaction': {'code': 0x96, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCommitTransaction': {'code': 0x97, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Wait', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCompactKeys': {'code': 0x98, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Count', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyArray', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCompareObjects': {'code': 0x99, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FirstObjectHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecondObjectHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtCompareSigningLevels': {'code': 0x9A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtCompareTokens': {'code': 0x9B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FirstTokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecondTokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Equal', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': False},
		]},

	'NtCompleteConnectPort': {'code': 0x9C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCompressKey': {'code': 0x9D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Key', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtConnectPort': {'code': 0x9E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'PortName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityQos', 'type':'PSECURITY_QUALITY_OF_SERVICE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientView', 'type':'PPORT_SECTION_WRITE', 'in': True, 'out': True, 'optional': True},
			{'name': 'ServerView', 'type':'PPORT_SECTION_READ', 'in': True, 'out': True, 'optional': True},
			{'name': 'MaxMessageLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'ConnectionInformation', 'type':'PVOID', 'in': True, 'out': True, 'optional': True},
			{'name': 'ConnectionInformationLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': True},
		]},

	#TODO: Unknown function until now
	'NtConvertBetweenAuxiliaryCounterAndPerformanceCounter': {'code': 0x9F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtCreateDebugObject': {'code': 0xA0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DebugObjectHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateDirectoryObject': {'code': 0xA1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DirectoryHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateDirectoryObjectEx': {'code': 0xA2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DirectoryHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'ShadowDirectoryHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtCreateEnclave': {'code': 0xA3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateEnlistment': {'code': 0xA4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'NotificationMask', 'type':'NOTIFICATION_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'EnlistmentKey', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateEventPair': {'code': 0xA5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventPairHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateIRTimer': {'code': 0xA6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateIoCompletion': {'code': 0xA7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'IoCompletionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'Count', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateJobObject': {'code': 0xA8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'JobHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateJobSet': {'code': 0xA9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'NumJob', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'UserJobSet', 'type':'PJOB_SET_ARRAY', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateKeyTransacted': {'code': 0xAA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'TitleIndex', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Class', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Disposition', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtCreateKeyedEvent': {'code': 0xAB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyedEventHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateLowBoxToken': {'code': 0xAC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TokenHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ExistingTokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'PackageSid', 'type':'PSID', 'in': True, 'out': False, 'optional': False},
			{'name': 'CapabilityCount', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Capabilities', 'type':'PSID_AND_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'HandleCount', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Handles', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateMailslotFile': {'code': 0xAD, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MailslotQuota', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaximumMessageSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReadTimeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateMutant': {'code': 0xAE, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'MutantHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'InitialOwner', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateNamedPipeFile': {'code': 0xAF, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'ShareAccess', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'CreateDisposition', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'NamedPipeType', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReadMode', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'CompletionMode', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaximumInstances', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'InboundQuota', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'OutboundQuota', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'DefaultTimeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreatePagingFile': {'code': 0xB0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PageFileName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'MinimumSize', 'type':'PULARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaximumSize', 'type':'PULARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Priority', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreatePartition': {'code': 0xB1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PartitionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'PreferredNode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreatePort': {'code': 0xB2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'MaxConnectionInfoLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaxMessageLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaxPoolUsage', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreatePrivateNamespace': {'code': 0xB3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'NamespaceHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'BoundaryDescriptor', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateProcess': {'code': 0xB4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'ParentProcess', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'InheritObjectTable', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'SectionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'DebugPort', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ExceptionPort', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateProfile': {'code': 0xB5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProfileHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'Process', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ProfileBase', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProfileSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'BucketSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'BufferSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProfileSource', 'type':'KPROFILE_SOURCE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Affinity', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateProfileEx': {'code': 0xB6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProfileHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'Process', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ProfileBase', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProfileSize', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': False},
			{'name': 'BucketSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'BufferSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProfileSource', 'type':'KPROFILE_SOURCE', 'in': True, 'out': False, 'optional': False},
			{'name': 'GroupCount', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
			{'name': 'GroupAffinity', 'type':'PGROUP_AFFINITY', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateRegistryTransaction': {'code': 0xB7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Handle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateResourceManager': {'code': 0xB8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ResourceManagerHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'RmGuid', 'type':'LPGUID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'Description', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateSemaphore': {'code': 0xB9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SemaphoreHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'InitialCount', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaximumCount', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateSymbolicLinkObject': {'code': 0xBA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'LinkHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'LinkTarget', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateThreadEx': {'code': 0xBB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'StartRoutine', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Argument', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'CreateFlags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ZeroBits', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': False},
			{'name': 'StackSize', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaximumStackSize', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': False},
			{'name': 'AttributeList', 'type':'PPS_ATTRIBUTE_LIST', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateTimer': {'code': 0xBC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'TimerType', 'type':'TIMER_TYPE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateTimer2': {'code': 0xBD, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'Reserved1', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'Reserved2', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'Attributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateToken': {'code': 0xBE, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TokenHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'TokenType', 'type':'TOKEN_TYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'AuthenticationId', 'type':'PLUID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ExpirationTime', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'User', 'type':'PTOKEN_USER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Groups', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': False},
			{'name': 'Privileges', 'type':'PTOKEN_PRIVILEGES', 'in': True, 'out': False, 'optional': False},
			{'name': 'Owner', 'type':'PTOKEN_OWNER', 'in': True, 'out': False, 'optional': True},
			{'name': 'PrimaryGroup', 'type':'PTOKEN_PRIMARY_GROUP', 'in': True, 'out': False, 'optional': False},
			{'name': 'DefaultDacl', 'type':'PTOKEN_DEFAULT_DACL', 'in': True, 'out': False, 'optional': True},
			{'name': 'TokenSource', 'type':'PTOKEN_SOURCE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateTokenEx': {'code': 0xBF, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TokenHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'TokenType', 'type':'TOKEN_TYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'AuthenticationId', 'type':'PLUID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ExpirationTime', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'User', 'type':'PTOKEN_USER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Groups', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': False},
			{'name': 'Privileges', 'type':'PTOKEN_PRIVILEGES', 'in': True, 'out': False, 'optional': False},
			{'name': 'UserAttributes', 'type':'PTOKEN_SECURITY_ATTRIBUTES_INFORMATION', 'in': True, 'out': False, 'optional': True},
			{'name': 'DeviceAttributes', 'type':'PTOKEN_SECURITY_ATTRIBUTES_INFORMATION', 'in': True, 'out': False, 'optional': True},
			{'name': 'DeviceGroups', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': True},
			{'name': 'TokenMandatoryPolicy', 'type':'PTOKEN_MANDATORY_POLICY', 'in': True, 'out': False, 'optional': True},
			{'name': 'Owner', 'type':'PTOKEN_OWNER', 'in': True, 'out': False, 'optional': True},
			{'name': 'PrimaryGroup', 'type':'PTOKEN_PRIMARY_GROUP', 'in': True, 'out': False, 'optional': False},
			{'name': 'DefaultDacl', 'type':'PTOKEN_DEFAULT_DACL', 'in': True, 'out': False, 'optional': True},
			{'name': 'TokenSource', 'type':'PTOKEN_SOURCE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateTransaction': {'code': 0xC0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'Uow', 'type':'LPGUID', 'in': True, 'out': False, 'optional': True},
			{'name': 'TmHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'IsolationLevel', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'IsolationFlags', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'Description', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateTransactionManager': {'code': 0xC1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TmHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'LogFileName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'CommitStrength', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateUserProcess': {'code': 0xC2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ThreadHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ProcessDesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadDesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProcessObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'ThreadObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'ProcessFlags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadFlags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProcessParameters', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'CreateInfo', 'type':'PPS_CREATE_INFO', 'in': True, 'out': True, 'optional': False},
			{'name': 'AttributeList', 'type':'PPS_ATTRIBUTE_LIST', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateWaitCompletionPacket': {'code': 0xC3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'WaitCompletionPacketHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateWaitablePort': {'code': 0xC4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'MaxConnectionInfoLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaxMessageLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaxPoolUsage', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtCreateWnfStateName': {'code': 0xC5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'StateName', 'type':'PCWNF_STATE_NAME', 'in': False, 'out': True, 'optional': False},
			{'name': 'NameLifetime', 'type':'WNF_STATE_NAME_LIFETIME', 'in': True, 'out': False, 'optional': False},
			{'name': 'DataScope', 'type':'WNF_DATA_SCOPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PersistData', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'TypeId', 'type':'PCWNF_TYPE_ID', 'in': True, 'out': False, 'optional': True},
			{'name': 'MaximumStateSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateWorkerFactory': {'code': 0xC6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'WorkerFactoryHandleReturn', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'CompletionPortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'WorkerProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'StartRoutine', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'StartParameter', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'MaxThreadCount', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'StackReserve', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': True},
			{'name': 'StackCommit', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': True},
		]},

	'NtDebugActiveProcess': {'code': 0xC7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DebugObjectHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDebugContinue': {'code': 0xC8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DebugObjectHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientId', 'type':'PCLIENT_ID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ContinueStatus', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDeleteAtom': {'code': 0xC9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Atom', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDeleteBootEntry': {'code': 0xCA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Id', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDeleteDriverEntry': {'code': 0xCB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Id', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDeleteFile': {'code': 0xCC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDeleteKey': {'code': 0xCD, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDeleteObjectAuditAlarm': {'code': 0xCE, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SubsystemName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleId', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'GenerateOnClose', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDeletePrivateNamespace': {'code': 0xCF, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'NamespaceHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDeleteValueKey': {'code': 0xD0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ValueName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDeleteWnfStateData': {'code': 0xD1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'StateName', 'type':'PCWNF_STATE_NAME', 'in': True, 'out': False, 'optional': False},
			{'name': 'ExplicitScope', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
		]},

	'NtDeleteWnfStateName': {'code': 0xD2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'StateName', 'type':'PCWNF_STATE_NAME', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDisableLastKnownGood': {'code': 0xD3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtDisplayString': {'code': 0xD4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'String', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDrawText': {'code': 0xD5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'String', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtEnableLastKnownGood': {'code': 0xD6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtEnumerateBootEntries': {'code': 0xD7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'BufferLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
		]},

	'NtEnumerateDriverEntries': {'code': 0xD8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'BufferLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
		]},

	'NtEnumerateSystemEnvironmentValuesEx': {'code': 0xD9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'InformationClass', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'BufferLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
		]},

	'NtEnumerateTransactionObject': {'code': 0xDA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'RootObjectHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'QueryType', 'type':'KTMOBJECT_TYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectCursor', 'type':'PKTMOBJECT_CURSOR', 'in': True, 'out': True, 'optional': False},
			{'name': 'ObjectCursorLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtExtendSection': {'code': 0xDB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SectionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewSectionSize', 'type':'PLARGE_INTEGER', 'in': True, 'out': True, 'optional': False},
		]},

	'NtFilterBootOption': {'code': 0xDC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FilterOperation', 'type':'FILTER_BOOT_OPTION_OPERATION', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ElementType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SystemData', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'DataSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtFilterToken': {'code': 0xDD, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ExistingTokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SidsToDisable', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': True},
			{'name': 'PrivilegesToDelete', 'type':'PTOKEN_PRIVILEGES', 'in': True, 'out': False, 'optional': True},
			{'name': 'RestrictedSids', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': True},
			{'name': 'NewTokenHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtFilterTokenEx': {'code': 0xDE, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': True},
			{'name': 'None', 'type':'PTOKEN_PRIVILEGES', 'in': True, 'out': False, 'optional': True},
			{'name': 'None', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': True},
			{'name': 'None', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'None', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'None', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': True},
			{'name': 'None', 'type':'PTOKEN_SECURITY_ATTRIBUTES_INFORMATION', 'in': True, 'out': False, 'optional': True},
			{'name': 'None', 'type':'PTOKEN_SECURITY_ATTRIBUTES_INFORMATION', 'in': True, 'out': False, 'optional': True},
			{'name': 'None', 'type':'PTOKEN_GROUPS', 'in': True, 'out': False, 'optional': True},
			{'name': 'None', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtFlushBuffersFileEx': {'code': 0xDF, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Parameters', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ParametersSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
		]},

	'NtFlushInstallUILanguage': {'code': 0xE0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'InstallUILanguage', 'type':'LANGID', 'in': True, 'out': False, 'optional': False},
			{'name': 'SetComittedFlag', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtFlushInstructionCache': {'code': 0xE1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtFlushKey': {'code': 0xE2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtFlushProcessWriteBuffers': {'code': 0xE3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtFlushVirtualMemory': {'code': 0xE4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PIO_STATUS_BLOCK', 'in': True, 'out': False, 'optional': False},
		]},

	'NtFlushWriteBuffer': {'code': 0xE5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtFreeUserPhysicalPages': {'code': 0xE6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfPages', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'UserPfnArray', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtFreezeRegistry': {'code': 0xE7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimeOutInSeconds', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtFreezeTransactions': {'code': 0xE8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FreezeTimeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThawTimeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGetCachedSigningLevel': {'code': 0xE9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'File', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'SigningLevel', 'type':'PSE_SIGNING_LEVEL', 'in': False, 'out': True, 'optional': False},
			{'name': 'Thumbprint', 'type':'PUCHAR', 'in': False, 'out': True, 'optional': True},
			{'name': 'ThumbprintSize', 'type':'PULONG', 'in': True, 'out': True, 'optional': True},
			{'name': 'ThumbprintAlgorithm', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGetCompleteWnfStateSubscription': {'code': 0xEA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'OldDescriptorStateName', 'type':'PCWNF_STATE_NAME', 'in': True, 'out': False, 'optional': True},
			{'name': 'OldSubscriptionId', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'OldDescriptorEventMask', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'OldDescriptorStatus', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'NewDeliveryDescriptor', 'type':'PWNF_DELIVERY_DESCRIPTOR', 'in': False, 'out': True, 'optional': False},
			{'name': 'DescriptorSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGetContextThread': {'code': 0xEB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadContext', 'type':'PCONTEXT', 'in': True, 'out': True, 'optional': False},
		]},

	'NtGetCurrentProcessorNumber': {'code': 0xEC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGetCurrentProcessorNumberEx': {'code': 0xED, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGetDevicePowerState': {'code': 0xEE, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Device', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'State', 'type':'PDEVICE_POWER_STATE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGetMUIRegistryInfo': {'code': 0xEF, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'DataSize', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'SystemData', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGetNextProcess': {'code': 0xF0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleAttributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewProcessHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGetNextThread': {'code': 0xF1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleAttributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewThreadHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGetNlsSectionPtr': {'code': 0xF2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SectionType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SectionData', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ContextData', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'SectionPointer', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'SectionSize', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGetNotificationResourceManager': {'code': 0xF3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ResourceManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionNotification', 'type':'PTRANSACTION_NOTIFICATION', 'in': False, 'out': True, 'optional': False},
			{'name': 'NotificationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'Asynchronous', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'AsynchronousContext', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtGetWriteWatch': {'code': 0xF4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'RegionSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'UserAddressArray', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'EntriesInUserAddressArray', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'Granularity', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtImpersonateAnonymousToken': {'code': 0xF5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtImpersonateThread': {'code': 0xF6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ServerThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityQos', 'type':'PSECURITY_QUALITY_OF_SERVICE', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtInitializeEnclave': {'code': 0xF7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtInitializeNlsFiles': {'code': 0xF8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'BaseAddress', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'DefaultLocaleId', 'type':'PLCID', 'in': False, 'out': True, 'optional': False},
			{'name': 'DefaultCasingTableSize', 'type':'PLARGE_INTEGER', 'in': False, 'out': True, 'optional': False},
		]},

	'NtInitializeRegistry': {'code': 0xF9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'BootCondition', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtInitiatePowerAction': {'code': 0xFA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SystemAction', 'type':'POWER_ACTION', 'in': True, 'out': False, 'optional': False},
			{'name': 'LightestSystemState', 'type':'SYSTEM_POWER_STATE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Asynchronous', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtIsSystemResumeAutomatic': {'code': 0xFB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtIsUILanguageComitted': {'code': 0xFC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtListenPort': {'code': 0xFD, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ConnectionRequest', 'type':'PPORT_MESSAGE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtLoadDriver': {'code': 0xFE, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DriverServiceName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtLoadEnclaveData': {'code': 0xFF, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtLoadHotPatch': {'code': 0x100, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtLoadKey': {'code': 0x101, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TargetKey', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'SourceFile', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtLoadKey2': {'code': 0x102, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TargetKey', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'SourceFile', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtLoadKeyEx': {'code': 0x103, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TargetKey', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'SourceFile', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'TrustClassKey', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': True},
			{'name': 'RootHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': True},
			{'name': 'IoStatus', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': True},
		]},

	'NtLockFile': {'code': 0x104, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'ByteOffset', 'type':'PULARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'PULARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Key', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'FailImmediately', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'ExclusiveLock', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtLockProductActivationKeys': {'code': 0x105, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'pPrivateVer', 'type':'PULONG', 'in': True, 'out': True, 'optional': True},
			{'name': 'pSafeMode', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtLockRegistryKey': {'code': 0x106, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtLockVirtualMemory': {'code': 0x107, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'RegionSize', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MapType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtMakePermanentObject': {'code': 0x108, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Handle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtMakeTemporaryObject': {'code': 0x109, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Handle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtManagePartition': {'code': 0x10A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TargetHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SourceHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PartitionInformationClass', 'type':'MEMORY_PARTITION_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'PartitionInformation', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
			{'name': 'PartitionInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtMapCMFModule': {'code': 0x10B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'What', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Index', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'CacheIndexOut', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'CacheFlagsOut', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'ViewSizeOut', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
		]},

	'NtMapUserPhysicalPages': {'code': 0x10C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'VirtualAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfPages', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'UserPfnArray', 'type':'PULONG', 'in': True, 'out': False, 'optional': True},
		]},

	#TODO: Unknown function until now
	'NtMapViewOfSectionEx': {'code': 0x10D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtModifyBootEntry': {'code': 0x10E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'BootEntry', 'type':'PBOOT_ENTRY', 'in': True, 'out': False, 'optional': False},
		]},

	'NtModifyDriverEntry': {'code': 0x10F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DriverEntry', 'type':'PEFI_DRIVER_ENTRY', 'in': True, 'out': False, 'optional': False},
		]},

	'NtNotifyChangeDirectoryFile': {'code': 0x110, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'Buffer', 'type':'PFILE_NOTIFY_INFORMATION', 'in': False, 'out': True, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'CompletionFilter', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'WatchTree', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtNotifyChangeDirectoryFileEx': {'code': 0x111, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtNotifyChangeKey': {'code': 0x112, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'CompletionFilter', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'WatchTree', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'BufferSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Asynchronous', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtNotifyChangeMultipleKeys': {'code': 0x113, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'MasterKeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Count', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'SubordinateObjects', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PIO_APC_ROUTINE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'CompletionFilter', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'WatchTree', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'BufferSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Asynchronous', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtNotifyChangeSession': {'code': 0x114, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SessionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ChangeSequenceNumber', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ChangeTimeStamp', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'IO_SESSION_EVENT', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewState', 'type':'IO_SESSION_STATE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousState', 'type':'IO_SESSION_STATE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Payload', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'PayloadSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenEnlistment': {'code': 0x115, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'EnlistmentGuid', 'type':'LPGUID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
		]},

	'NtOpenEventPair': {'code': 0x116, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventPairHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenIoCompletion': {'code': 0x117, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'IoCompletionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenJobObject': {'code': 0x118, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'JobHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenKeyEx': {'code': 0x119, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'OpenOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenKeyTransacted': {'code': 0x11A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenKeyTransactedEx': {'code': 0x11B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'OpenOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenKeyedEvent': {'code': 0x11C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyedEventHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenMutant': {'code': 0x11D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'MutantHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenObjectAuditAlarm': {'code': 0x11E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SubsystemName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleId', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ObjectTypeName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': True},
			{'name': 'ClientToken', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'GrantedAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'Privileges', 'type':'PPRIVILEGE_SET', 'in': True, 'out': False, 'optional': True},
			{'name': 'ObjectCreation', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'AccessGranted', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'GenerateOnClose', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': False},
		]},

	'NtOpenPartition': {'code': 0x11F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PartitionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenPrivateNamespace': {'code': 0x120, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'NamespaceHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'BoundaryDescriptor', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenProcessToken': {'code': 0x121, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtOpenRegistryTransaction': {'code': 0x122, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenResourceManager': {'code': 0x123, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ResourceManagerHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceManagerGuid', 'type':'LPGUID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
		]},

	'NtOpenSemaphore': {'code': 0x124, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SemaphoreHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenSession': {'code': 0x125, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SessionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenSymbolicLinkObject': {'code': 0x126, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'LinkHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenThread': {'code': 0x127, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientId', 'type':'PCLIENT_ID', 'in': True, 'out': False, 'optional': True},
		]},

	'NtOpenTimer': {'code': 0x128, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtOpenTransaction': {'code': 0x129, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'Uow', 'type':'LPGUID', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtOpenTransactionManager': {'code': 0x12A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TmHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'LogFileName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'TmIdentity', 'type':'LPGUID', 'in': True, 'out': False, 'optional': True},
			{'name': 'OpenOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtPlugPlayControl': {'code': 0x12B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PnPControlClass', 'type':'PLUGPLAY_CONTROL_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'PnPControlData', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
			{'name': 'PnPControlDataLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtPrePrepareComplete': {'code': 0x12C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtPrePrepareEnlistment': {'code': 0x12D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtPrepareComplete': {'code': 0x12E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtPrepareEnlistment': {'code': 0x12F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtPrivilegeCheck': {'code': 0x130, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ClientToken', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'RequiredPrivileges', 'type':'PPRIVILEGE_SET', 'in': True, 'out': True, 'optional': False},
			{'name': 'Result', 'type':'PBOOLEAN', 'in': False, 'out': True, 'optional': False},
		]},

	'NtPrivilegeObjectAuditAlarm': {'code': 0x131, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SubsystemName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleId', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ClientToken', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'Privileges', 'type':'PPRIVILEGE_SET', 'in': True, 'out': False, 'optional': False},
			{'name': 'AccessGranted', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtPrivilegedServiceAuditAlarm': {'code': 0x132, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SubsystemName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ServiceName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientToken', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Privileges', 'type':'PPRIVILEGE_SET', 'in': True, 'out': False, 'optional': False},
			{'name': 'AccessGranted', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtPropagationComplete': {'code': 0x133, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ResourceManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'RequestCookie', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'BufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtPropagationFailed': {'code': 0x134, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ResourceManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'RequestCookie', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'PropStatus', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtPulseEvent': {'code': 0x135, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousState', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	#TODO: Unknown function until now
	'NtQueryAuxiliaryCounterFrequency': {'code': 0x136, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtQueryBootEntryOrder': {'code': 0x137, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Ids', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'Count', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
		]},

	'NtQueryBootOptions': {'code': 0x138, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'BootOptions', 'type':'PBOOT_OPTIONS', 'in': False, 'out': True, 'optional': True},
			{'name': 'BootOptionsLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
		]},

	'NtQueryDebugFilterState': {'code': 0x139, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ComponentId', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Level', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtQueryDirectoryFileEx': {'code': 0x13A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtQueryDirectoryObject': {'code': 0x13B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DirectoryHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnSingleEntry', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'RestartScan', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'Context', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryDriverEntryOrder': {'code': 0x13C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Ids', 'type':'PULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'Count', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
		]},

	'NtQueryEaFile': {'code': 0x13D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'Buffer', 'type':'PFILE_FULL_EA_INFORMATION', 'in': False, 'out': True, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnSingleEntry', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'EaList', 'type':'PFILE_GET_EA_INFORMATION', 'in': True, 'out': False, 'optional': True},
			{'name': 'EaListLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'EaIndex', 'type':'PULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'RestartScan', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueryFullAttributesFile': {'code': 0x13E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileInformation', 'type':'PFILE_NETWORK_OPEN_INFORMATION', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryInformationAtom': {'code': 0x13F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Atom', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
			{'name': 'AtomInformationClass', 'type':'ATOM_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'AtomInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'AtomInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	#TODO: Unknown function until now
	'NtQueryInformationByName': {'code': 0x140, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtQueryInformationEnlistment': {'code': 0x141, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'EnlistmentInformationClass', 'type':'ENLISTMENT_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'EnlistmentInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'EnlistmentInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryInformationJobObject': {'code': 0x142, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'JobHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'JobObjectInformationClass', 'type':'JOBOBJECTINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'JobObjectInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'JobObjectInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryInformationPort': {'code': 0x143, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortInformationClass', 'type':'PORT_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'PortInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryInformationResourceManager': {'code': 0x144, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ResourceManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceManagerInformationClass', 'type':'RESOURCEMANAGER_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceManagerInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'ResourceManagerInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryInformationTransaction': {'code': 0x145, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionInformationClass', 'type':'TRANSACTION_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'TransactionInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryInformationTransactionManager': {'code': 0x146, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionManagerInformationClass', 'type':'TRANSACTIONMANAGER_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionManagerInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'TransactionManagerInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryInformationWorkerFactory': {'code': 0x147, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'WorkerFactoryHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'WorkerFactoryInformationClass', 'type':'WORKERFACTORYINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'WorkerFactoryInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'WorkerFactoryInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryInstallUILanguage': {'code': 0x148, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'InstallUILanguageId', 'type':'PLANGID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryIntervalProfile': {'code': 0x149, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProfileSource', 'type':'KPROFILE_SOURCE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Interval', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryIoCompletion': {'code': 0x14A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'IoCompletionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoCompletionInformationClass', 'type':'IO_COMPLETION_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoCompletionInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'IoCompletionInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryLicenseValue': {'code': 0x14B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ValueName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'Type', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'SystemData', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'DataSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResultDataSize', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryMultipleValueKey': {'code': 0x14C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ValueEntries', 'type':'PKEY_VALUE_ENTRY', 'in': True, 'out': True, 'optional': False},
			{'name': 'EntryCount', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ValueBuffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'BufferLength', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'RequiredBufferLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryMutant': {'code': 0x14D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'MutantHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'MutantInformationClass', 'type':'MUTANT_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'MutantInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'MutantInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryOpenSubKeys': {'code': 0x14E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TargetKey', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'HandleCount', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryOpenSubKeysEx': {'code': 0x14F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TargetKey', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'BufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'RequiredSize', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryPortInformationProcess': {'code': 0x150, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtQueryQuotaInformationFile': {'code': 0x151, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'Buffer', 'type':'PFILE_USER_QUOTA_INFORMATION', 'in': False, 'out': True, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnSingleEntry', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'SidList', 'type':'PFILE_QUOTA_LIST_INFORMATION', 'in': True, 'out': False, 'optional': True},
			{'name': 'SidListLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'StartSid', 'type':'PSID', 'in': True, 'out': False, 'optional': True},
			{'name': 'RestartScan', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQuerySecurityAttributesToken': {'code': 0x152, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Attributes', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'NumberOfAttributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQuerySecurityObject': {'code': 0x153, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Handle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityInformation', 'type':'SECURITY_INFORMATION', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityDescriptor', 'type':'PSECURITY_DESCRIPTOR', 'in': False, 'out': True, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'LengthNeeded', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQuerySecurityPolicy': {'code': 0x154, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQuerySemaphore': {'code': 0x155, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SemaphoreHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SemaphoreInformationClass', 'type':'SEMAPHORE_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'SemaphoreInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'SemaphoreInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQuerySymbolicLinkObject': {'code': 0x156, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'LinkHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'LinkTarget', 'type':'PUNICODE_STRING', 'in': True, 'out': True, 'optional': False},
			{'name': 'ReturnedLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQuerySystemEnvironmentValue': {'code': 0x157, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'VariableName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'VariableValue', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'ValueLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQuerySystemEnvironmentValueEx': {'code': 0x158, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'VariableName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'VendorGuid', 'type':'LPGUID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Value', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'ValueLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'Attributes', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQuerySystemInformationEx': {'code': 0x159, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SystemInformationClass', 'type':'SYSTEM_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'InputBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'InputBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SystemInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'SystemInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtQueryTimerResolution': {'code': 0x15A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'MaximumTime', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'MinimumTime', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'CurrentTime', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtQueryWnfStateData': {'code': 0x15B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'StateName', 'type':'PCWNF_STATE_NAME', 'in': True, 'out': False, 'optional': False},
			{'name': 'TypeId', 'type':'PCWNF_TYPE_ID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ExplicitScope', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ChangeStamp', 'type':'PWNF_CHANGE_STAMP', 'in': False, 'out': True, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'BufferSize', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
		]},

	'NtQueryWnfStateNameInformation': {'code': 0x15C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'StateName', 'type':'PCWNF_STATE_NAME', 'in': True, 'out': False, 'optional': False},
			{'name': 'NameInfoClass', 'type':'PCWNF_TYPE_ID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ExplicitScope', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'InfoBuffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'InfoBufferSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtQueueApcThreadEx': {'code': 0x15D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'UserApcReserveHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcRoutine', 'type':'PKNORMAL_ROUTINE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ApcArgument1', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcArgument2', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcArgument3', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
		]},

	'NtRaiseException': {'code': 0x15E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ExceptionRecord', 'type':'PEXCEPTION_RECORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'ContextRecord', 'type':'PCONTEXT', 'in': True, 'out': False, 'optional': False},
			{'name': 'FirstChance', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRaiseHardError': {'code': 0x15F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ErrorStatus', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfParameters', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'UnicodeStringParameterMask', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Parameters', 'type':'PULONG_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'ValidResponseOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Response', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtReadOnlyEnlistment': {'code': 0x160, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtRecoverEnlistment': {'code': 0x161, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'EnlistmentKey', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
		]},

	'NtRecoverResourceManager': {'code': 0x162, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ResourceManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRecoverTransactionManager': {'code': 0x163, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRegisterProtocolAddressInformation': {'code': 0x164, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ResourceManager', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProtocolId', 'type':'LPGUID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProtocolInformationSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ProtocolInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'CreateOptions', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
		]},

	'NtRegisterThreadTerminatePort': {'code': 0x165, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReleaseKeyedEvent': {'code': 0x166, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyedEventHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyValue', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Alertable', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtReleaseWorkerFactoryWorker': {'code': 0x167, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'WorkerFactoryHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRemoveIoCompletionEx': {'code': 0x168, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'IoCompletionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoCompletionInformation', 'type':'PFILE_IO_COMPLETION_INFORMATION', 'in': False, 'out': True, 'optional': False},
			{'name': 'Count', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumEntriesRemoved', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'Alertable', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRemoveProcessDebug': {'code': 0x169, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DebugObjectHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRenameKey': {'code': 0x16A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRenameTransactionManager': {'code': 0x16B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'LogFileName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ExistingTransactionManagerGuid', 'type':'LPGUID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReplaceKey': {'code': 0x16C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'NewFile', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'TargetHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'OldFile', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReplacePartitionUnit': {'code': 0x16D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TargetInstancePath', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'SpareInstancePath', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtReplyWaitReplyPort': {'code': 0x16E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReplyMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': True, 'optional': False},
		]},

	'NtRequestPort': {'code': 0x16F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'RequestMessage', 'type':'PPORT_MESSAGE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtResetEvent': {'code': 0x170, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousState', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtResetWriteWatch': {'code': 0x171, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'RegionSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRestoreKey': {'code': 0x172, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtResumeProcess': {'code': 0x173, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRevertContainerImpersonation': {'code': 0x174, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtRollbackComplete': {'code': 0x175, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtRollbackEnlistment': {'code': 0x176, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	#TODO: Unknown parameter types
	'NtRollbackRegistryTransaction': {'code': 0x177, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRollbackTransaction': {'code': 0x178, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Wait', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtRollforwardTransactionManager': {'code': 0x179, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtSaveKey': {'code': 0x17A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSaveKeyEx': {'code': 0x17B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Format', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSaveMergedKeys': {'code': 0x17C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'HighPrecedenceKeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'LowPrecedenceKeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSecureConnectPort': {'code': 0x17D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'PHANDLE', 'in': False, 'out': True, 'optional': False},
			{'name': 'PortName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityQos', 'type':'PSECURITY_QUALITY_OF_SERVICE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClientView', 'type':'PPORT_SECTION_WRITE', 'in': True, 'out': True, 'optional': True},
			{'name': 'RequiredServerSid', 'type':'PSID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ServerView', 'type':'PPORT_SECTION_READ', 'in': True, 'out': True, 'optional': True},
			{'name': 'MaxMessageLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'ConnectionInformation', 'type':'PVOID', 'in': True, 'out': True, 'optional': True},
			{'name': 'ConnectionInformationLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': True},
		]},

	'NtSerializeBoot': {'code': 0x17E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtSetBootEntryOrder': {'code': 0x17F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Ids', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Count', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetBootOptions': {'code': 0x180, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'BootOptions', 'type':'PBOOT_OPTIONS', 'in': True, 'out': False, 'optional': False},
			{'name': 'FieldsToChange', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetCachedSigningLevel': {'code': 0x181, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'InputSigningLevel', 'type':'SE_SIGNING_LEVEL', 'in': True, 'out': False, 'optional': False},
			{'name': 'SourceFiles', 'type':'PHANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SourceFileCount', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'TargetFile', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	#TODO: Unknown parameter types
	'NtSetCachedSigningLevel2': {'code': 0x182, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetContextThread': {'code': 0x183, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Context', 'type':'PCONTEXT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetDebugFilterState': {'code': 0x184, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ComponentId', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Level', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'State', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetDefaultHardErrorPort': {'code': 0x185, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'PortHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetDefaultLocale': {'code': 0x186, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'UserProfile', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'DefaultLocaleId', 'type':'LCID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetDefaultUILanguage': {'code': 0x187, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DefaultUILanguageId', 'type':'LANGID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetDriverEntryOrder': {'code': 0x188, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Ids', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Count', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetEaFile': {'code': 0x189, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'EaBuffer', 'type':'PFILE_FULL_EA_INFORMATION', 'in': True, 'out': False, 'optional': False},
			{'name': 'EaBufferSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetHighEventPair': {'code': 0x18A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventPairHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetHighWaitLowEventPair': {'code': 0x18B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventPairHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetIRTimer': {'code': 0x18C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DueTime', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtSetInformationDebugObject': {'code': 0x18D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DebugObject', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'InformationClass', 'type':'DEBUGOBJECTINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'Information', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'InformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtSetInformationEnlistment': {'code': 0x18E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'EnlistmentInformationClass', 'type':'ENLISTMENT_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'EnlistmentInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'EnlistmentInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationJobObject': {'code': 0x18F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'JobHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'JobObjectInformationClass', 'type':'JOBOBJECTINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'JobObjectInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'JobObjectInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationKey': {'code': 0x190, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'KeyHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeySetInformationClass', 'type':'KEY_SET_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeySetInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeySetInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationResourceManager': {'code': 0x191, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ResourceManagerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceManagerInformationClass', 'type':'RESOURCEMANAGER_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceManagerInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResourceManagerInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtSetInformationSymbolicLink': {'code': 0x192, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationToken': {'code': 0x193, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TokenHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenInformationClass', 'type':'TOKEN_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'TokenInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationTransaction': {'code': 0x194, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionInformationClass', 'type':'TRANSACTIONMANAGER_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationTransactionManager': {'code': 0x195, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TransactionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionInformationClass', 'type':'TRANSACTION_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransactionInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationVirtualMemory': {'code': 0x196, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'VmInformationClass', 'type':'VIRTUAL_MEMORY_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfEntries', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'VirtualAddresses', 'type':'PMEMORY_RANGE_ENTRY', 'in': True, 'out': False, 'optional': False},
			{'name': 'VmInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'VmInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetInformationWorkerFactory': {'code': 0x197, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'WorkerFactoryHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'WorkerFactoryInformationClass', 'type':'WORKERFACTORYINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'WorkerFactoryInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'WorkerFactoryInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetIntervalProfile': {'code': 0x198, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Interval', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Source', 'type':'KPROFILE_SOURCE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetIoCompletion': {'code': 0x199, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'IoCompletionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'CompletionKey', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'CompletionStatus', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfBytesTransfered', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetIoCompletionEx': {'code': 0x19A, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'IoCompletionHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoCompletionPacketHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ApcContext', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'IoStatus', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusInformation', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetLdtEntries': {'code': 0x19B, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Selector0', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Entry0Low', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Entry0Hi', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Selector1', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Entry1Low', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Entry1Hi', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetLowEventPair': {'code': 0x19C, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventPairHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetLowWaitHighEventPair': {'code': 0x19D, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EventPairHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetQuotaInformationFile': {'code': 0x19E, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'Buffer', 'type':'PFILE_USER_QUOTA_INFORMATION', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetSecurityObject': {'code': 0x19F, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ObjectHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'SecurityInformationClass', 'type':'SECURITY_INFORMATION', 'in': True, 'out': False, 'optional': False},
			{'name': 'DescriptorBuffer', 'type':'PSECURITY_DESCRIPTOR', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetSystemEnvironmentValue': {'code': 0x1A0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'VariableName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'Value', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetSystemEnvironmentValueEx': {'code': 0x1A1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'VariableName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'VendorGuid', 'type':'LPGUID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Value', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ValueLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Attributes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetSystemInformation': {'code': 0x1A2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SystemInformationClass', 'type':'SYSTEM_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'SystemInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'SystemInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetSystemPowerState': {'code': 0x1A3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SystemAction', 'type':'POWER_ACTION', 'in': True, 'out': False, 'optional': False},
			{'name': 'MinSystemState', 'type':'SYSTEM_POWER_STATE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetSystemTime': {'code': 0x1A4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SystemTime', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousTime', 'type':'PLARGE_INTEGER', 'in': False, 'out': True, 'optional': True},
		]},

	'NtSetThreadExecutionState': {'code': 0x1A5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ExecutionState', 'type':'EXECUTION_STATE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousExecutionState', 'type':'PEXECUTION_STATE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtSetTimer2': {'code': 0x1A6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'DueTime', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Period', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'Parameters', 'type':'PT2_SET_PARAMETERS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetTimerEx': {'code': 0x1A7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TimerHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TimerSetInformationClass', 'type':'TIMER_SET_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'TimerSetInformation', 'type':'PVOID', 'in': True, 'out': True, 'optional': True},
			{'name': 'TimerSetInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetTimerResolution': {'code': 0x1A8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DesiredResolution', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SetResolution', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'CurrentResolution', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtSetUuidSeed': {'code': 0x1A9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Seed', 'type':'PUCHAR', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetVolumeInformationFile': {'code': 0x1AA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'FileSystemInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'FileSystemInformationClass', 'type':'FS_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSetWnfProcessNotificationEvent': {'code': 0x1AB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'NotificationEvent', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtShutdownSystem': {'code': 0x1AC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Action', 'type':'SHUTDOWN_ACTION', 'in': True, 'out': False, 'optional': False},
		]},

	'NtShutdownWorkerFactory': {'code': 0x1AD, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'WorkerFactoryHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PendingWorkerCount', 'type':'PLONG', 'in': True, 'out': True, 'optional': False},
		]},

	'NtSignalAndWaitForSingleObject': {'code': 0x1AE, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'hObjectToSignal', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'hObjectToWaitOn', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'bAlertable', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwMilliseconds', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtSinglePhaseReject': {'code': 0x1AF, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'EnlistmentHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'TmVirtualClock', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
		]},

	'NtStartProfile': {'code': 0x1B0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProfileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtStopProfile': {'code': 0x1B1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProfileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSubscribeWnfStateChange': {'code': 0x1B2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'StateName', 'type':'PCWNF_STATE_NAME', 'in': True, 'out': False, 'optional': False},
			{'name': 'ChangeStamp', 'type':'WNF_CHANGE_STAMP', 'in': True, 'out': False, 'optional': True},
			{'name': 'EventMask', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SubscriptionId', 'type':'PLARGE_INTEGER', 'in': False, 'out': True, 'optional': True},
		]},

	'NtSuspendProcess': {'code': 0x1B3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtSuspendThread': {'code': 0x1B4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'PreviousSuspendCount', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtSystemDebugControl': {'code': 0x1B5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Command', 'type':'DEBUG_CONTROL_CODE', 'in': True, 'out': False, 'optional': False},
			{'name': 'InputBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'InputBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'OutputBuffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'OutputBufferLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ReturnLength', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	#TODO: Unknown function until now
	'NtTerminateEnclave': {'code': 0x1B6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtTerminateJobObject': {'code': 0x1B7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'JobHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ExitStatus', 'type':'NTSTATUS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtTestAlert': {'code': 0x1B8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtThawRegistry': {'code': 0x1B9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	'NtThawTransactions': {'code': 0x1BA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
		]},

	#'NtTraceControl': {'code': 0x1BB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
	#	[
	#		{'name': 'None', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
	#		{'name': 'None', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
	#		{'name': 'None', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
	#		{'name': 'None', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
	#		{'name': 'None', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
	#		{'name': 'None', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
	#	]},

	'NtTranslateFilePath': {'code': 0x1BC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'InputFilePath', 'type':'PFILE_PATH', 'in': True, 'out': False, 'optional': False},
			{'name': 'OutputType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'OutputFilePath', 'type':'PFILE_PATH', 'in': False, 'out': True, 'optional': True},
			{'name': 'OutputFilePathLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': True},
		]},

	'NtUmsThreadYield': {'code': 0x1BD, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'SchedulerParam', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUnloadDriver': {'code': 0x1BE, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DriverServiceName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUnloadKey': {'code': 0x1BF, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DestinationKeyName', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUnloadKey2': {'code': 0x1C0, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TargetKey', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUnloadKeyEx': {'code': 0x1C1, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'TargetKey', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'Event', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtUnlockFile': {'code': 0x1C2, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'FileHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IoStatusBlock', 'type':'PIO_STATUS_BLOCK', 'in': False, 'out': True, 'optional': False},
			{'name': 'ByteOffset', 'type':'PULARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Length', 'type':'PULARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'Key', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUnlockVirtualMemory': {'code': 0x1C3, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'NumberOfBytesToUnlock', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'LockType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUnmapViewOfSectionEx': {'code': 0x1C4, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'ProcessHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'BaseAddress', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUnsubscribeWnfStateChange': {'code': 0x1C5, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'StateName', 'type':'PCWNF_STATE_NAME', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUpdateWnfStateData': {'code': 0x1C6, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'StateName', 'type':'PCWNF_STATE_NAME', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'Length', 'type':'ULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'TypeId', 'type':'PCWNF_TYPE_ID', 'in': True, 'out': False, 'optional': True},
			{'name': 'ExplicitScope', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'MatchingChangeStamp', 'type':'WNF_CHANGE_STAMP', 'in': True, 'out': False, 'optional': False},
			{'name': 'CheckStamp', 'type':'LOGICAL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtVdmControl': {'code': 0x1C7, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'Service', 'type':'VDMSERVICECLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ServiceData', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtWaitForAlertByThreadId': {'code': 0x1C8, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtWaitForDebugEvent': {'code': 0x1C9, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'DebugObjectHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Alertable', 'type':'BOOLEAN', 'in': True, 'out': False, 'optional': False},
			{'name': 'Timeout', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': True},
			{'name': 'WaitStateChange', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtWaitForKeyedEvent': {'code': 0x1CA, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtWaitForWorkViaWorkerFactory': {'code': 0x1CB, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtWaitHighEventPair': {'code': 0x1CC, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtWaitLowEventPair': {'code': 0x1CD, 'retVal':'NTSTATUS', 'lib': 'ntdll.dll', 'params':
		[
			{'name': 'None', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

}
