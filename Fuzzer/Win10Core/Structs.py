Data = \
{	'LARGE_INTEGER':
		[
			{'name': 'LowPart', 'type': 'DWORD'},
			{'name': 'HighPart', 'type': 'LONG'}
		]
	, 'PLARGE_INTEGER': 'LARGE_INTEGER*', 'PULARGE_INTEGER': 'LARGE_INTEGER*',

	'GUID':
		[
			{'name': 'Data1', 'type': 'DWORD'},
			{'name': 'Data2', 'type': 'WORD'},
			{'name': 'Data3', 'type': 'WORD'},
			{'name': 'Data4', 'type': 'BYTE', 'array': 8},
		]
	, 'PGUID': 'GUID*', 'LPGUID': 'GUID*',

	'UNICODE_STRING':
		[
			{'name': 'Length', 'type': 'int16'},
			{'name': 'MaximumLength', 'type': 'int16'},
			{'name': 'Buffer', 'type': 'pwstr'}
		]
	, 'PUNICODE_STRING': 'UNICODE_STRING*',

	'OBJECT_ATTRIBUTES':
		[
			{'name': 'Length', 'type': 'ULONG'},
			{'name': 'RootDirectory', 'type': 'DWORD'},
			{'name': 'ObjectName', 'type': 'PUNICODE_STRING'},
			{'name': 'Attributes', 'type': 'ULONG'},
			{'name': 'SecurityDescriptor', 'type': 'PVOID'},
			{'name': 'SecurityQualityOfService', 'type': 'PVOID'}
		]
	, 'POBJECT_ATTRIBUTES': 'OBJECT_ATTRIBUTES*',

	'IO_STATUS_BLOCK':
		[
			{'name': 'Status', 'type': 'NTSTATUS'},
			{'name': 'Information', 'type': 'ULONG_PTR'}
		]
	, 'PIO_STATUS_BLOCK': 'IO_STATUS_BLOCK*',

	'SID_IDENTIFIER_AUTHORITY':
		[
			{'name': 'IdentifierAuthority', 'type': 'UCHAR', 'array': 6},
		]
	, 'PSID_IDENTIFIER_AUTHORITY': 'SID_IDENTIFIER_AUTHORITY*',

	'SID':
		[
			{'name': 'Revision', 'type': 'UCHAR'},
			{'name': 'SubAuthorityCount', 'type': 'UCHAR'},
			{'name': 'IdentifierAuthority', 'type': 'SID_IDENTIFIER_AUTHORITY'},
			{'name': 'SubAuthority', 'type': 'ULONG', 'array': 0x20}  # TODO: Support unknown array sizes
		]
	, 'PSID': 'SID*',

	'ACL':
		[
			{'name': 'AclRevision', 'type': 'BYTE'},
			{'name': 'Sbz1', 'type': 'BYTE'},
			{'name': 'AclSize', 'type': 'WORD'},
			{'name': 'AceCount', 'type': 'WORD'},
			{'name': 'Sbz2', 'type': 'WORD'}
		]
	, 'PACL': 'ACL*',

	'SECURITY_DESCRIPTOR':
		[
			{'name': 'Revision', 'type': 'UCHAR'},
			{'name': 'Sbz1', 'type': 'UCHAR'},
			{'name': 'Control', 'type': 'USHORT'},
			{'name': 'Owner', 'type': 'PSID'},
			{'name': 'Group', 'type': 'PSID'},
			{'name': 'Sacl', 'type': 'PACL'},
			{'name': 'Dacl', 'type': 'PACL'}
		]
	, 'PSECURITY_DESCRIPTOR': 'SECURITY_DESCRIPTOR*',

	'OBJECT_TYPE_LIST':
		[
			{'name': 'Level', 'type': 'WORD'},
			{'name': 'Sbz', 'type': 'WORD'},
			{'name': 'ObjectType', 'type': 'LPGUID'}
		]
	, 'POBJECT_TYPE_LIST': 'OBJECT_TYPE_LIST*',

	'GENERIC_MAPPING':
		[
			{'name': 'GenericRead', 'type': 'ACCESS_MASK'},
			{'name': 'GenericWrite', 'type': 'ACCESS_MASK'},
			{'name': 'GenericExecute', 'type': 'ACCESS_MASK'},
			{'name': 'GenericAll', 'type': 'ACCESS_MASK'}
		]
	, 'PGENERIC_MAPPING': 'GENERIC_MAPPING*',

	'IO_APC_ROUTINE':
		[
			{'name': 'UnknownElements', 'type': 'DWORD', 'array': 10}
		]
	, 'PIO_APC_ROUTINE': 'IO_APC_ROUTINE*',

	'SECURITY_QUALITY_OF_SERVICE':
		[
			{'name': 'Length', 'type': 'DWORD'},
			{'name': 'ImpersonationLevel', 'type': 'SECURITY_IMPERSONATION_LEVEL'},
			{'name': 'ContextTrackingMode', 'type': 'SECURITY_CONTEXT_TRACKING_MODE'},
			{'name': 'EffectiveOnly', 'type': 'BOOLEAN'}
		]
	, 'PSECURITY_QUALITY_OF_SERVICE': 'SECURITY_QUALITY_OF_SERVICE*',

	'PORT_SECTION_WRITE':
		[
			{'name': 'Length', 'type': 'ULONG'},
			{'name': 'hSection', 'type': 'HANDLE'},
			{'name': 'SectionOffset', 'type': 'ULONG'},
			{'name': 'ViewSize', 'type': 'ULONG'},
			{'name': 'ViewBase', 'type': 'PVOID'},
			{'name': 'TargetViewBase', 'type': 'PVOID'}
		]
	, 'PPORT_SECTION_WRITE': 'PORT_SECTION_WRITE*',

	'PORT_SECTION_READ':
		[
			{'name': 'Length', 'type': 'ULONG'},
			{'name': 'ViewSize', 'type': 'ULONG'},
			{'name': 'ViewBase', 'type': 'PVOID'}
		]
	, 'PPORT_SECTION_READ': 'PORT_SECTION_READ*',

	'CLIENT_ID':
		[
			{'name': 'UniqueProcess', 'type': 'HANDLE'},
			{'name': 'UniqueThread', 'type': 'HANDLE'}
		]
	, 'PCLIENT_ID': 'CLIENT_ID*',

	'PORT_MESSAGE':
		[
			{'name': 'DPPRIVILEGE_SETualRangesOffset', 'type': 'USHORT'},
			{'name': 'ClientId', 'type': 'CLIENT_ID'},
			{'name': 'MessageId', 'type': 'ULONG'},
			{'name': 'SectionSize', 'type': 'ULONG'},
		]
	, 'PPORT_MESSAGE': 'PORT_MESSAGE*',

	'LUID':
		[
			{'name': 'LowPart', 'type': 'DWORD'},
			{'name': 'HighPart', 'type': 'LONG'}
		]
	, 'PLUID': 'LUID*',

	'LUID_AND_ATTRIBUTES':
		[
			{'name': 'Luid', 'type': 'LUID'},
			{'name': 'Attributes', 'type': 'DWORD'}
		]
	, 'PLUID_AND_ATTRIBUTES': 'LUID_AND_ATTRIBUTES*',

	'PRIVILEGE_SET':
		[
			{'name': 'PrivilegeCount', 'type': 'DWORD'},
			{'name': 'Control', 'type': 'DWORD'},
			{'name': 'Privilege', 'type': 'LUID_AND_ATTRIBUTES', 'array': 0x20}  # TODO: Support unknown array sizes
		]
	, 'PPRIVILEGE_SET': 'PRIVILEGE_SET*',

	'SID_AND_ATTRIBUTES':
		[
			{'name': 'Sid', 'type': 'PSID'},
			{'name': 'Attributes', 'type': 'DWORD'}
		]
	, 'PSID_AND_ATTRIBUTES': 'SID_AND_ATTRIBUTES*',

	'TOKEN_USER':
		[
			{'name': 'User', 'type': 'SID_AND_ATTRIBUTES'}
		]
	, 'PTOKEN_USER': 'TOKEN_USER*',

	'TOKEN_GROUPS':
		[
			{'name': 'GroupCount', 'type': 'DWORD'},
			{'name': 'Groups', 'type': 'SID_AND_ATTRIBUTES', 'array': 0x20}  # TODO: Support unknown array sizes
		]
	, 'PTOKEN_GROUPS': 'TOKEN_GROUPS*',

	'TOKEN_PRIVILEGES':
		[
			{'name': 'PrivilegeCount', 'type': 'DWORD'},
			{'name': 'Privileges', 'type': 'LUID_AND_ATTRIBUTES', 'array': 0x20}  # TODO: Support unknown array sizes
		]
	, 'PTOKEN_PRIVILEGES': 'TOKEN_PRIVILEGES*',

	'TOKEN_OWNER':
		[
			{'name': 'Owner', 'type': 'PSID'}
		]
	, 'PTOKEN_OWNER': 'TOKEN_OWNER*',

	'TOKEN_PRIMARY_GROUP':
		[
			{'name': 'PrimaryGroup', 'type': 'PSID'}
		]
	, 'PTOKEN_PRIMARY_GROUP': 'TOKEN_PRIMARY_GROUP*',

	'TOKEN_DEFAULT_DACL':
		[
			{'name': 'DefaultDacl', 'type': 'PACL'}
		]
	, 'PTOKEN_DEFAULT_DACL': 'TOKEN_DEFAULT_DACL*',

	'TOKEN_SOURCE':
		[
			{'name': 'SourceName', 'type': 'CHAR', 'array': 8},
			{'name': 'SourceIdentifier', 'type': 'LUID'}
		]
	, 'PTOKEN_SOURCE': 'TOKEN_SOURCE*',

	'FLOATING_SAVE_AREA':
		[
			{'name': 'ControlWord', 'type': 'ULONG'},
			{'name': 'StatusWord', 'type': 'ULONG'},
			{'name': 'TagWord', 'type': 'ULONG'},
			{'name': 'ErrorOffset', 'type': 'ULONG'},
			{'name': 'ErrorSelector', 'type': 'ULONG'},
			{'name': 'DataOffset', 'type': 'ULONG'},
			{'name': 'DataSelector', 'type': 'ULONG'},
			{'name': 'RegisterArea', 'type': 'UCHAR', 'array': 80},
			{'name': 'Cr0NpxState', 'type': 'ULONG'}
		]
	, 'PFLOATING_SAVE_AREA': 'FLOATING_SAVE_AREA*',

	'CONTEXT':
		[
			{'name': 'ContextFlags', 'type': 'ULONG'},
			{'name': 'Dr0', 'type': 'ULONG'},
			{'name': 'Dr1', 'type': 'ULONG'},
			{'name': 'Dr2', 'type': 'ULONG'},
			{'name': 'Dr3', 'type': 'ULONG'},
			{'name': 'Dr6', 'type': 'ULONG'},
			{'name': 'Dr7', 'type': 'ULONG'},
			{'name': 'FloatSave', 'type': 'FLOATING_SAVE_AREA'},
			{'name': 'SegGs', 'type': 'ULONG'},
			{'name': 'SegFs', 'type': 'ULONG'},
			{'name': 'SegEs', 'type': 'ULONG'},
			{'name': 'SegDs', 'type': 'ULONG'},
			{'name': 'Edi', 'type': 'ULONG'},
			{'name': 'Esi', 'type': 'ULONG'},
			{'name': 'Ebx', 'type': 'ULONG'},
			{'name': 'Edx', 'type': 'ULONG'},
			{'name': 'Ecx', 'type': 'ULONG'},
			{'name': 'Eax', 'type': 'ULONG'},
			{'name': 'Ebp', 'type': 'ULONG'},
			{'name': 'Eip', 'type': 'ULONG'},
			{'name': 'SegCs', 'type': 'ULONG'},
			{'name': 'EFlags', 'type': 'ULONG'},
			{'name': 'Esp', 'type': 'ULONG'},
			{'name': 'SegSs', 'type': 'ULONG'},
			{'name': 'ExtendedRegisters', 'type': 'UCHAR', 'array': 512}
		]
	, 'PCONTEXT': 'CONTEXT*',

	'FILE_NOTIFY_INFORMATION':
		[
			{'name': 'NextEntryOffset', 'type': 'DWORD'},
			{'name': 'Action', 'type': 'DWORD'},
			{'name': 'FileNameLength', 'type': 'DWORD'},
			{'name': 'FileName', 'type': 'WCHAR'}
		]
	, 'PFILE_NOTIFY_INFORMATION': 'FILE_NOTIFY_INFORMATION*',

	'KEY_VALUE_ENTRY':
		[
			{'name': 'ValueName', 'type': 'PUNICODE_STRING'},
			{'name': 'DataLength', 'type': 'ULONG'},
			{'name': 'DataOffset', 'type': 'ULONG'},
			{'name': 'Type', 'type': 'ULONG'}
		]
	, 'PKEY_VALUE_ENTRY': 'KEY_VALUE_ENTRY*',

	'FILE_SEGMENT_ELEMENT':  # TODO: This is incorrect but I don't have a glue how to represent it at this point :D
		[
			{'name': 'part1', 'type': 'PVOID'},
			{'name': 'part2', 'type': 'PVOID'}
		]
	, 'PFILE_SEGMENT_ELEMENT': 'FILE_SEGMENT_ELEMENT*',

	'USER_STACK':
		[
			{'name': 'FixedStackBase', 'type': 'PVOID'},
			{'name': 'FixedStackLimit', 'type': 'PVOID'},
			{'name': 'ExpandableStackBase', 'type': 'PVOID'},
			{'name': 'ExpandableStackLimit', 'type': 'PVOID'},
			{'name': 'ExpandableStackBottom', 'type': 'PVOID'}
		]
	, 'PUSER_STACK': 'USER_STACK*',

	'FILE_BASIC_INFORMATION':
		[
			{'name': 'CreationTime', 'type': 'LARGE_INTEGER'},
			{'name': 'LastAccessTime', 'type': 'LARGE_INTEGER'},
			{'name': 'LastWriteTime', 'type': 'LARGE_INTEGER'},
			{'name': 'ChangeTime', 'type': 'LARGE_INTEGER'},
			{'name': 'FileAttributes', 'type': 'ULONG'}
		]
	, 'PFILE_BASIC_INFORMATION': 'FILE_BASIC_INFORMATION*',

	'FILE_NETWORK_OPEN_INFORMATION':
		[
			{'name': 'CreationTime', 'type': 'LARGE_INTEGER'},
			{'name': 'LastAccessTime', 'type': 'LARGE_INTEGER'},
			{'name': 'LastWriteTime', 'type': 'LARGE_INTEGER'},
			{'name': 'ChangeTime', 'type': 'LARGE_INTEGER'},
			{'name': 'AllocationSize', 'type': 'LARGE_INTEGER'},
			{'name': 'EndOfFile', 'type': 'LARGE_INTEGER'},
			{'name': 'FileAttributes', 'type': 'ULONG'}
		]
	, 'PFILE_NETWORK_OPEN_INFORMATION': 'FILE_NETWORK_OPEN_INFORMATION*',

	'FILE_USER_QUOTA_INFORMATION':
		[
			{'name': 'NextEntryOffset', 'type': 'ULONG'},
			{'name': 'SidLength', 'type': 'ULONG'},
			{'name': 'ChangeTime', 'type': 'LARGE_INTEGER'},
			{'name': 'QuotaUsed', 'type': 'LARGE_INTEGER'},
			{'name': 'QuotaThreshold', 'type': 'LARGE_INTEGER'},
			{'name': 'QuotaLimit', 'type': 'LARGE_INTEGER'},
			{'name': 'Sid', 'type': 'SID'}
		]
	, 'PFILE_USER_QUOTA_INFORMATION': 'FILE_USER_QUOTA_INFORMATION*',

	'FILE_QUOTA_LIST_INFORMATION':
		[
			{'name': 'NextEntryOffset', 'type': 'ULONG'},
			{'name': 'SidLength', 'type': 'ULONG'},
			{'name': 'Sid', 'type': 'SID'}
		]
	, 'PFILE_QUOTA_LIST_INFORMATION': 'FILE_QUOTA_LIST_INFORMATION*',

	'FILE_FULL_EA_INFORMATION':
		[
			{'name': 'NextEntryOffset', 'type': 'ULONG'},
			{'name': 'Flags', 'type': 'ULONG'},
			{'name': 'EaNameLength', 'type': 'UCHAR'},
			{'name': 'EaValueLength', 'type': 'USHORT'},
			{'name': 'EaName', 'type': 'CHAR'}
		]
	, 'PFILE_FULL_EA_INFORMATION': 'FILE_FULL_EA_INFORMATION*',

	'FILE_GET_EA_INFORMATION':
		[
			{'name': 'NextEntryOffset', 'type': 'ULONG'},
			{'name': 'EaNameLength', 'type': 'UCHAR'},
			{'name': 'EaName', 'type': 'CHAR'}
		]
	, 'PFILE_GET_EA_INFORMATION': 'FILE_GET_EA_INFORMATION*',

	'LDT_ENTRY':
		[
			{'name': 'LimitLow', 'type': 'WORD'},
			{'name': 'BaseLow', 'type': 'WORD'},
			{'name': 'HighWord', 'type': 'DWORD'}
		]
	, 'PLDT_ENTRY': 'LDT_ENTRY*',

	'EXCEPTION_RECORD':
		[
			{'name': 'LimitLow', 'type': 'DWORD'},
			{'name': 'BaseLow', 'type': 'DWORD'},
			{'name': 'ExceptionRecord', 'type': 'DWORD'},
			# TODO: This should be PEXCEPTION_RECORD type actually but code can't handle recursive records yet
			{'name': 'ExceptionAddress', 'type': 'PVOID'},
			{'name': 'NumberParameters', 'type': 'DWORD'},
			{'name': 'ExceptionInformation', 'type': 'DWORD', 'array': 15}
		]
	, 'PEXCEPTION_RECORD': 'EXCEPTION_RECORD*',

	'T2_SET_PARAMETERS':
		[
			{'name': 'Version', 'type': 'ULONG'},
			{'name': 'Reserved', 'type': 'ULONG'},
			{'name': 'NoWakeTolerance1', 'type': 'DWORD'},
			{'name': 'NoWakeTolerance2', 'type': 'DWORD'}
		]
	, 'PT2_SET_PARAMETERS': 'T2_SET_PARAMETERS*',

	'FILE_PATH':
		[
			{'name': 'Version', 'type': 'ULONG'},
			{'name': 'Length', 'type': 'ULONG'},
			{'name': 'Type', 'type': 'ULONG'},
			{'name': 'FilePath', 'type': 'UCHAR'}
		]
	, 'PFILE_PATH': 'FILE_PATH*',

	'BOOT_OPTIONS':
		[
			{'name': 'Version', 'type': 'ULONG'},
			{'name': 'Length', 'type': 'ULONG'},
			{'name': 'Timeout', 'type': 'ULONG'},
			{'name': 'CurrentBootEntryId', 'type': 'ULONG'},
			{'name': 'NextBootEntryId', 'type': 'ULONG'},
			{'name': 'HeadlessRedirection', 'type': 'WCHAR'}
		]
	, 'PBOOT_OPTIONS': 'BOOT_OPTIONS*',

	'CWNF_STATE_NAME':
		[
			{'name': 'SystemData', 'type': 'ULONG', 'array': 2},
		]
	, 'PCWNF_STATE_NAME': 'CWNF_STATE_NAME*',

	'CWNF_TYPE_ID':
		[
			{'name': 'TypeId', 'type': 'GUID'},
		]
	, 'PCWNF_TYPE_ID': 'CWNF_TYPE_ID*',

	'FILE_IO_COMPLETION_INFORMATION':
		[
			{'name': 'KeyContext', 'type': 'PVOID'},
			{'name': 'ApcContext', 'type': 'PVOID'},
			{'name': 'IoStatusBlock', 'type': 'IO_STATUS_BLOCK'},
		]
	, 'PFILE_IO_COMPLETION_INFORMATION': 'FILE_IO_COMPLETION_INFORMATION*',

	'MEMORY_RANGE_ENTRY':
		[
			{'name': 'VirtualAddress', 'type': 'PVOID'},
			{'name': 'NumberOfBytes', 'type': 'SIZE_T'},
		]
	, 'PMEMORY_RANGE_ENTRY': 'MEMORY_RANGE_ENTRY*',

	'TRANSACTION_NOTIFICATION':
		[
			{'name': 'TransactionKey', 'type': 'PVOID'},
			{'name': 'TransactionNotification', 'type': 'ULONG'},
			{'name': 'TmVirtualClock', 'type': 'LARGE_INTEGER'},
			{'name': 'ArgumentLength', 'type': 'ULONG'},
		]
	, 'PTRANSACTION_NOTIFICATION': 'TRANSACTION_NOTIFICATION*',

	'WNF_DELIVERY_DESCRIPTOR':
		[
			{'name': 'SubscriptionId1', 'type': 'ULONG'},  # TODO: Should be one ULONGLONG but you know, 64bit values
			{'name': 'SubscriptionId2', 'type': 'PVOID'},
			{'name': 'StateName', 'type': 'CWNF_STATE_NAME'},
			{'name': 'ChangeStamp', 'type': 'WNF_CHANGE_STAMP'},
			{'name': 'StateDataSize', 'type': 'ULONG'},
			{'name': 'EventMask', 'type': 'ULONG'},
			{'name': 'TypeId', 'type': 'CWNF_TYPE_ID'},
			{'name': 'StateDataOffset', 'type': 'ULONG'},
		]
	, 'PWNF_DELIVERY_DESCRIPTOR': 'WNF_DELIVERY_DESCRIPTOR*',

	'EFI_DRIVER_ENTRY':
		[
			{'name': 'Version', 'type': 'ULONG'},
			{'name': 'Length', 'type': 'ULONG'},
			{'name': 'Id', 'type': 'ULONG'},
			{'name': 'FriendlyNameOffset', 'type': 'ULONG'},
			{'name': 'DriverFilePathOffset', 'type': 'ULONG'},
		]
	, 'PEFI_DRIVER_ENTRY': 'EFI_DRIVER_ENTRY*',

	'BOOT_ENTRY':
		[
			{'name': 'Version', 'type': 'ULONG'},
			{'name': 'Length', 'type': 'ULONG'},
			{'name': 'Id', 'type': 'ULONG'},
			{'name': 'Attributes', 'type': 'ULONG'},
			{'name': 'FriendlyNameOffset', 'type': 'ULONG'},
			{'name': 'BootFilePathOffset', 'type': 'ULONG'},
			{'name': 'OsOptionsLength', 'type': 'ULONG'},
			{'name': 'OsOptions', 'type': 'UCHAR'},
		]
	, 'PBOOT_ENTRY': 'BOOT_ENTRY*',

	'SuccessState':
		[
			{'name': 'OutputFlags', 'type': 'ULONG'},
			{'name': 'FileHandle', 'type': 'HANDLE'},
			{'name': 'SectionHandle', 'type': 'HANDLE'},
			{'name': 'UserProcessParametersNative1', 'type': 'ULONG'},  # TODO: Actually 64bit
			{'name': 'UserProcessParametersNative2', 'type': 'ULONG'},
			{'name': 'UserProcessParametersWow64', 'type': 'ULONG'},
			{'name': 'CurrentParameterFlags', 'type': 'ULONG'},
			{'name': 'PebAddressNative1', 'type': 'ULONG'},  # TODO: Actually 64bit
			{'name': 'PebAddressNative2', 'type': 'ULONG'},
			{'name': 'PebAddressWow64', 'type': 'ULONG'},
			{'name': 'ManifestAddress1', 'type': 'ULONG'},  # TODO: Actually 64bit
			{'name': 'ManifestAddress2', 'type': 'ULONG'},
			{'name': 'ManifestSize', 'type': 'ULONG'},
		]
	, 'PSuccessState': 'SuccessState*',

	'PS_CREATE_INFO':
		[
			{'name': 'Size', 'type': 'SIZE_T'},
			{'name': 'State', 'type': 'PS_CREATE_STATE'},
			{'name': 'Union', 'type': 'SuccessState'},
		]
	, 'PPS_CREATE_INFO': 'PS_CREATE_INFO*',

	'KTMOBJECT_CURSOR':
		[
			{'name': 'LastQuery', 'type': 'GUID'},
			{'name': 'ObjectIdCount', 'type': 'ULONG'},
			{'name': 'ObjectIds', 'type': 'GUID'},
		]
	, 'PKTMOBJECT_CURSOR': 'KTMOBJECT_CURSOR*',

	'PS_ATTRIBUTE':
		[
			{'name': 'Attribute', 'type': 'ULONG'},
			{'name': 'Size', 'type': 'SIZE_T'},
			{'name': 'ValuePtr', 'type': 'PVOID'},
			{'name': 'ReturnLength', 'type': 'PSIZE_T'},
		]
	, 'PPS_ATTRIBUTE': 'PS_ATTRIBUTE*',

	'PS_ATTRIBUTE_LIST':
		[
			{'name': 'LastQuery', 'type': 'SIZE_T'},
			{'name': 'Attributes', 'type': 'PS_ATTRIBUTE'},
		]
	, 'PPS_ATTRIBUTE_LIST': 'PS_ATTRIBUTE_LIST*',

	'TOKEN_SECURITY_ATTRIBUTE_V1':
		[
			{'name': 'Name', 'type': 'UNICODE_STRING'},
			{'name': 'ValueType', 'type': 'USHORT'},
			{'name': 'Reserved', 'type': 'USHORT'},
			{'name': 'Flags', 'type': 'ULONG'},
			{'name': 'ValueCount', 'type': 'ULONG'},
			{'name': 'pString', 'type': 'PUNICODE_STRING'},
			{'name': 'someValue', 'type': 'LONG'},
		]
	, 'PTOKEN_SECURITY_ATTRIBUTE_V1': 'TOKEN_SECURITY_ATTRIBUTE_V1*',

	'TOKEN_SECURITY_ATTRIBUTES_INFORMATION':
		[
			{'name': 'Version', 'type': 'USHORT'},
			{'name': 'Reserved', 'type': 'USHORT'},
			{'name': 'AttributeCount', 'type': 'ULONG'},
			{'name': 'Attribute', 'type': 'PTOKEN_SECURITY_ATTRIBUTE_V1'},
		]
	, 'PTOKEN_SECURITY_ATTRIBUTES_INFORMATION': 'TOKEN_SECURITY_ATTRIBUTES_INFORMATION*',

	'ALPC_MESSAGE_ATTRIBUTES':
		[
			{'name': 'AllocatedAttributes', 'type': 'ULONG'},
			{'name': 'ValidAttributes', 'type': 'ULONG'},
		]
	, 'PALPC_MESSAGE_ATTRIBUTES': 'ALPC_MESSAGE_ATTRIBUTES*',

	'ALPC_DATA_VIEW_ATTR':
		[
			{'name': 'Flags', 'type': 'ULONG'},
			{'name': 'SectionHandle', 'type': 'HANDLE'},
			{'name': 'ViewBase', 'type': 'PVOID'},
			{'name': 'ViewSize', 'type': 'SIZE_T'},
		]
	, 'PALPC_DATA_VIEW_ATTR': 'ALPC_DATA_VIEW_ATTR*',

	'ALPC_SECURITY_ATTR':
		[
			{'name': 'Flags', 'type': 'ULONG'},
			{'name': 'QoS', 'type': 'PSECURITY_QUALITY_OF_SERVICE'},
			{'name': 'ContextHandle', 'type': 'HANDLE'},
		]
	, 'PALPC_SECURITY_ATTR': 'ALPC_SECURITY_ATTR*',

	'ALPC_PORT_ATTRIBUTES':
		[
			{'name': 'Flags', 'type': 'ULONG'},
			{'name': 'SecurityQos', 'type': 'PSECURITY_QUALITY_OF_SERVICE'},
			{'name': 'MaxMessageLength', 'type': 'SIZE_T'},
			{'name': 'MemoryBandwidth', 'type': 'SIZE_T'},
			{'name': 'MaxPoolUsage', 'type': 'SIZE_T'},
			{'name': 'MaxSectionSize', 'type': 'SIZE_T'},
			{'name': 'MaxViewSize', 'type': 'SIZE_T'},
			{'name': 'MaxTotalSectionSize', 'type': 'SIZE_T'},
			{'name': 'DupObjectTypes', 'type': 'ULONG'},
		]
	, 'PALPC_PORT_ATTRIBUTES': 'ALPC_PORT_ATTRIBUTES*',

	'GROUP_AFFINITY':
		[
			{'name': 'Mask', 'type': 'KAFFINITY'},
			{'name': 'Group', 'type': 'WORD'},
			{'name': 'Reserved', 'type': 'WORD', 'array': 3},
		]
	, 'PGROUP_AFFINITY': 'GROUP_AFFINITY*',

	'JOB_SET_ARRAY':
		[
			{'name': 'JobHandle', 'type': 'HANDLE'},
			{'name': 'MemberLevel', 'type': 'ULONG'},
			{'name': 'Flags', 'type': 'ULONG'},
			{'name': 'MemberLevel', 'type': 'DWORD'},
			{'name': 'Flags', 'type': 'DWORD'},
		]
	, 'PJOB_SET_ARRAY': 'JOB_SET_ARRAY*',

	'TOKEN_MANDATORY_POLICY':
		[
			{'name': 'Policy', 'type': 'DWORD'},
		]
	, 'PTOKEN_MANDATORY_POLICY': 'TOKEN_MANDATORY_POLICY*',

	'ALPC_CONTEXT_ATTR':
		[
			{'name': 'PortContext', 'type': 'PVOID'},
			{'name': 'MessageContext', 'type': 'PVOID'},
			{'name': 'Sequence', 'type': 'ULONG'},
			{'name': 'MessageId', 'type': 'ULONG'},
			{'name': 'CallbackId', 'type': 'ULONG'},
		]
	, 'PALPC_CONTEXT_ATTR': 'ALPC_CONTEXT_ATTR*'
}