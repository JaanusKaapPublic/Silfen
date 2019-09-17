Data = {
	#TODO: Unknown parameter types
	'NtUserGetOwnerTransformedMonitorRect': {'code': 0x1000, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserYieldTask': {'code': 0x1001, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserSetSensorPresence': {'code': 0x1002, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetThreadState': {'code': 0x1003, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Routine', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserPeekMessage': {'code': 0x1004, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pMsg', 'type':'PMSG', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'MsgFilterMin', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'MsgFilterMax', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'RemoveMsg', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCallOneParam': {'code': 0x1005, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Param', 'type':'DWORD_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'Routine', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetKeyState': {'code': 0x1006, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'VirtKey', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserInvalidateRect': {'code': 0x1007, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpRect', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'bErase', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCallNoParam': {'code': 0x1008, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Routine', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetMessage': {'code': 0x1009, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pMsg', 'type':'PMSG', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'MsgFilterMin', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'MsgFilterMax', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserMessageCall': {'code': 0x100A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Msg', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'wParam', 'type':'WPARAM', 'in': True, 'out': False, 'optional': False},
			{'name': 'lParam', 'type':'LPARAM', 'in': True, 'out': False, 'optional': False},
			{'name': 'ResultInfo', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwType', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Ansi', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiBitBlt': {'code': 0x100B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdcDst', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdcSrc', 'type':'HDC', 'in': True, 'out': False, 'optional': True},
			{'name': 'xSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'ySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'rop4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'crBackColor', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'fl', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetCharSet': {'code': 0x100C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetDC': {'code': 0x100D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSelectBitmap': {'code': 0x100E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserWaitMessage': {'code': 0x100F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserTranslateMessage': {'code': 0x1010, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpMsg', 'type':'LPMSG', 'in': True, 'out': False, 'optional': False},
			{'name': 'flags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetProp': {'code': 0x1011, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserPostMessage': {'code': 0x1012, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Msg', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'wParam', 'type':'WPARAM', 'in': True, 'out': False, 'optional': False},
			{'name': 'lParam', 'type':'LPARAM', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserQueryWindow': {'code': 0x1013, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Index', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserTranslateAccelerator': {'code': 0x1014, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Window', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Table', 'type':'HACCEL', 'in': True, 'out': False, 'optional': False},
			{'name': 'Message', 'type':'LPMSG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFlush': {'code': 0x1015, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserRedrawWindow': {'code': 0x1016, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lprcUpdate', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgnUpdate', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'flags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserWindowFromPoint': {'code': 0x1017, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'x', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCallMsgFilter': {'code': 0x1018, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'msg', 'type':'LPMSG', 'in': True, 'out': False, 'optional': False},
			{'name': 'code', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserValidateTimerCallback': {'code': 0x1019, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lParam', 'type':'LPARAM', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserBeginPaint': {'code': 0x101A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lPs', 'type':'PPAINTSTRUCT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetTimer': {'code': 0x101B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserEndPaint': {'code': 0x101C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lPs', 'type':'PPAINTSTRUCT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetCursor': {'code': 0x101D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hCursor', 'type':'HCURSOR', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserKillTimer': {'code': 0x101E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'uIDEvent', 'type':'UINT_PTR', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserBuildHwndList': {'code': 0x101F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSelectPalette': {'code': 0x1020, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hpal', 'type':'HPALETTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ForceBackground', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCallNextHookEx': {'code': 0x1021, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Code', 'type':'int', 'in': True, 'out': False, 'optional': False},
			{'name': 'wParam', 'type':'WPARAM', 'in': True, 'out': False, 'optional': False},
			{'name': 'lParam', 'type':'LPARAM', 'in': True, 'out': False, 'optional': False},
			{'name': 'Ansi', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserHideCaret': {'code': 0x1022, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiIntersectClipRect': {'code': 0x1023, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xLeft', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yTop', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xRight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yBottom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCallHwndLock': {'code': 0x1024, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Routine', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetProcessWindowStation': {'code': 0x1025, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiDeleteObjectApp': {'code': 0x1026, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hobj', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetWindowPos': {'code': 0x1027, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWndInsertAfter', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uFlags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserShowCaret': {'code': 0x1028, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserEndDeferWindowPosEx': {'code': 0x1029, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'WinPosInfo', 'type':'HDWP', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCallHwndParamLock': {'code': 0x102A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Param', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Routine', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserVkKeyScanEx': {'code': 0x102B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'wChar', 'type':'WCHAR', 'in': True, 'out': False, 'optional': False},
			{'name': 'KeyboardLayout', 'type':'HKL', 'in': True, 'out': False, 'optional': False},
			{'name': 'bUsehHK', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetDIBitsToDeviceInternal': {'code': 0x102C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdcDest', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cx', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'xSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'ySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'iStartScan', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'cNumScan', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pInitBits', 'type':'LPBYTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbmi', 'type':'LPBITMAPINFO', 'in': True, 'out': False, 'optional': False},
			{'name': 'iUsage', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjMaxBits', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjMaxInfo', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'bTransformCoordinates', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'hcmXform', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtUserCallTwoParam': {'code': 0x102D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Param1', 'type':'DWORD_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'Param2', 'type':'DWORD_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'Routine', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetRandomRgn': {'code': 0x102E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgnDest', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'iCode', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCopyAcceleratorTable': {'code': 0x102F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Table', 'type':'HACCEL', 'in': True, 'out': False, 'optional': False},
			{'name': 'Entries', 'type':'LPACCEL', 'in': True, 'out': False, 'optional': False},
			{'name': 'EntriesCount', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserNotifyWinEvent': {'code': 0x1030, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Event', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'idObject', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'idChild', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiExtSelectClipRgn': {'code': 0x1031, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': True},
			{'name': 'iMode', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserIsClipboardFormatAvailable': {'code': 0x1032, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'format', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetScrollInfo': {'code': 0x1033, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'fnBar', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpsi', 'type':'LPCSCROLLINFO', 'in': True, 'out': False, 'optional': False},
			{'name': 'bRedraw', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiStretchBlt': {'code': 0x1034, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdcDst', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cyDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdcSrc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'ySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwRop', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwBackColor', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCreateCaret': {'code': 0x1035, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hBitmap', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'nWidth', 'type':'int', 'in': True, 'out': False, 'optional': False},
			{'name': 'nHeight', 'type':'int', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiRectVisible': {'code': 0x1036, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'prc', 'type':'LPRECT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCombineRgn': {'code': 0x1037, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hrgnDst', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgnSrc1', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgnSrc2', 'type':'HRGN', 'in': True, 'out': False, 'optional': True},
			{'name': 'iMode', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetDCObject': {'code': 0x1038, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'itype', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDispatchMessage': {'code': 0x1039, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pMsg', 'type':'PMSG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRegisterWindowMessage': {'code': 0x103A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'MessageName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiExtTextOutW': {'code': 0x103B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'flOpts', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'prcl', 'type':'LPRECT', 'in': True, 'out': False, 'optional': True},
			{'name': 'pwsz', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'cwc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdx', 'type':'LPINT', 'in': True, 'out': False, 'optional': True},
			{'name': 'dwCodePage', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSelectFont': {'code': 0x103C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hf', 'type':'HFONT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiRestoreDC': {'code': 0x103D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'iLevel', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSaveDC': {'code': 0x103E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetForegroundWindow': {'code': 0x103F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserShowScrollBar': {'code': 0x1040, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'wBar', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'bShow', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserFindExistingCursorIcon': {'code': 0x1041, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pustrModule', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'pustrRsrc', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'param', 'type':'PFINDEXISTINGCURICONPARAM', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetDCDword': {'code': 0x1042, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'u', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'Result', 'type':'PDWORD', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetRegionData': {'code': 0x1043, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hrgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjBuffer', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpRgnData', 'type':'LPRGNDATA', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiLineTo': {'code': 0x1044, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSystemParametersInfo': {'code': 0x1045, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'uiAction', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uiParam', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvParam', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'fWinIni', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetAppClipBox': {'code': 0x1046, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'lprc', 'type':'LPRECT', 'in': False, 'out': True, 'optional': False},
		]},

	'NtUserGetAsyncKeyState': {'code': 0x1047, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Key', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetCPD': {'code': 0x1048, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'GETCPD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Proc', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRemoveProp': {'code': 0x1049, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Atom', 'type':'ATOM', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiDoPalette': {'code': 0x104A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hObj', 'type':'HGDIOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'iStart', 'type':'WORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'cEntries', 'type':'WORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pEntries', 'type':'LPVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'iFunc', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'bInbound', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPolyPolyDraw': {'code': 0x104B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppt', 'type':'PPOINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcpt', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ccpt', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'iFunc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetCapture': {'code': 0x104C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Wnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserEnumDisplayMonitors': {'code': 0x104D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateCompatibleBitmap': {'code': 0x104E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'cx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetProp': {'code': 0x104F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Atom', 'type':'ATOM', 'in': True, 'out': False, 'optional': False},
			{'name': 'Data', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetTextCharsetInfo': {'code': 0x1050, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpSig', 'type':'LPFONTSIGNATURE', 'in': False, 'out': True, 'optional': True},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSBGetParms': {'code': 0x1051, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'fnBar', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pSBData', 'type':'PSBDATA', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpsi', 'type':'LPSCROLLINFO', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetIconInfo': {'code': 0x1052, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserExcludeUpdateRgn': {'code': 0x1053, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetFocus': {'code': 0x1054, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiExtGetObjectW': {'code': 0x1055, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hobj', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjBufferSize', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpBuffer', 'type':'LPVOID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtUserGetUpdateRect': {'code': 0x1056, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpRect', 'type':'LPRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'fErase', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateCompatibleDC': {'code': 0x1057, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': True},
		]},

	'NtUserGetClipboardSequenceNumber': {'code': 0x1058, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiCreatePen': {'code': 0x1059, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'iPenStyle', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'iPenWidth', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cr', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbr', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserShowWindow': {'code': 0x105A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'nCmdShow', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetKeyboardLayoutList': {'code': 0x105B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'nItems', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pHklBuff', 'type':'PHKL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPatBlt': {'code': 0x105C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdcDest', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwRop', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserMapVirtualKeyEx': {'code': 0x105D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'keyCode', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'transType', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'keyboardId', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwhkl', 'type':'HKL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetWindowLong': {'code': 0x105E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Index', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewValue', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Ansi', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiHfontCreate': {'code': 0x105F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pelfw', 'type':'PENUMLOGFONTEXDVW', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjElfw', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'lft', 'type':'LFTYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'fl', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvCliData', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserMoveWindow': {'code': 0x1060, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nWidth', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nHeight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'bRepaint', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserPostThreadMessage': {'code': 0x1061, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'idThread', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Msg', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'wParam', 'type':'WPARAM', 'in': True, 'out': False, 'optional': False},
			{'name': 'lParam', 'type':'LPARAM', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDrawIconEx': {'code': 0x1062, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xLeft', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yTop', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hIcon', 'type':'HICON', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxWidth', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cyWidth', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'istepIfAniCur', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbrFlickerFreeDraw', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
			{'name': 'diFlags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'bMetaHDC', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pDIXData', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetSystemMenu': {'code': 0x1063, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'bRevert', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiDrawStream': {'code': 0x1064, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdcDst', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjIn', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvIn', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserInternalGetWindowText': {'code': 0x1065, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpString', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'nMaxCount', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetWindowDC': {'code': 0x1066, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiInvertRgn': {'code': 0x1067, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetRgnBox': {'code': 0x1068, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hRgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'pRect', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetAndSetDCDword': {'code': 0x1069, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'u', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwIn', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdwResult', 'type':'PDWORD', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiMaskBlt': {'code': 0x106A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdcSrc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'ySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbmMask', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': True},
			{'name': 'xMask', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yMask', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwRop4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'crBackColor', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetWidthTable': {'code': 0x106B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'cSpecial', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwc', 'type':'wstr', 'in': True, 'out': False, 'optional': False},
			{'name': 'cwc', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'psWidth', 'type':'PUSHORT', 'in': False, 'out': True, 'optional': False},
			{'name': 'pwd', 'type':'PWIDTHDATA', 'in': False, 'out': True, 'optional': True},
			{'name': 'pflInfo', 'type':'PFLONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtUserScrollDC': {'code': 0x106C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'dx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lprcScroll', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lprcClip', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgnUpdate', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'lprcUpdate', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetObjectInformation': {'code': 0x106D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hObject', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'nIndex', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'nLength', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'nLengthNeeded', 'type':'PDWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateBitmap': {'code': 0x106E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'cx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cPlanes', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cBPP', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjInit', 'type':'LPBYTE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtUserFindWindowEx': {'code': 0x106F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwndParent', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hwndChildAfter', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'ucClassName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ucWindowName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPolyPatBlt': {'code': 0x1070, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'rop4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pPoly', 'type':'PPOLYPATBLT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cPoly', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwMode', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUnhookWindowsHookEx': {'code': 0x1071, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Hook', 'type':'HHOOK', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetNearestColor': {'code': 0x1072, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'cr', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiTransformPoints': {'code': 0x1073, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'UnsafePtsIn', 'type':'PPOINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'UnsafePtOut', 'type':'PPOINT', 'in': False, 'out': True, 'optional': False},
			{'name': 'Count', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'iMode', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetDCPoint': {'code': 0x1074, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'iPoint', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'Point', 'type':'PPOINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateDIBBrush': {'code': 0x1075, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pv', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'fl', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cj', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'b8X8', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'bPen', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pClient', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetTextMetricsW': {'code': 0x1076, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pUnsafeTmwi', 'type':'PTMW_INTERNAL', 'in': False, 'out': True, 'optional': False},
			{'name': 'cj', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserCreateWindowEx': {'code': 0x1077, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
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
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetParent': {'code': 0x1078, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWndChild', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWndNewParent', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetKeyboardState': {'code': 0x1079, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'LPBYTE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserToUnicodeEx': {'code': 0x107A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'wVirtKey', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'wScanCode', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpKeyState', 'type':'PBYTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwszBuff', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cchBuff', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'wFlags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwhkl', 'type':'HKL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetControlBrush': {'code': 0x107B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'ctlType', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetClassName': {'code': 0x107C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Real', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClassName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiAlphaBlend': {'code': 0x107D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdcDst', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'DstX', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'DstY', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'DstCx', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'DstCy', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdcSrc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'SrcX', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SrcY', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SrcCx', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'SrcCy', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'BlendFunction', 'type':'BLENDFUNCTION', 'in': True, 'out': False, 'optional': False},
			{'name': 'hcmXform', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiOffsetRgn': {'code': 0x107E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hrgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'cx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDefSetText': {'code': 0x107F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'WindowHandle', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'WindowText', 'type':'PLARGE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetTextFaceW': {'code': 0x1080, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'Count', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'FaceName', 'type':'LPWSTR', 'in': False, 'out': True, 'optional': True},
			{'name': 'bAliasName', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiStretchDIBitsInternal': {'code': 0x1081, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cyDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'ySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjInit', 'type':'LPBYTE', 'in': True, 'out': False, 'optional': True},
			{'name': 'pbmi', 'type':'LPBITMAPINFO', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUsage', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwRop4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjMaxInfo', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjMaxBits', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hcmXform', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtUserSendInput': {'code': 0x1082, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'nInputs', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pInput', 'type':'LPINPUT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cbSize', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetThreadDesktop': {'code': 0x1083, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateRectRgn': {'code': 0x1084, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'xLeft', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yTop', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xRight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yBottom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetDIBitsInternal': {'code': 0x1085, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'iStartScan', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cScans', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjBits', 'type':'LPBYTE', 'in': False, 'out': True, 'optional': False},
			{'name': 'pbmi', 'type':'LPBITMAPINFO', 'in': True, 'out': True, 'optional': False},
			{'name': 'iUsage', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjMaxBits', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjMaxInfo', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetUpdateRgn': {'code': 0x1086, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hRgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'bErase', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiDeleteClientObj': {'code': 0x1087, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'h', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetIconSize': {'code': 0x1088, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Handle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'istepIfAniCur', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'plcx', 'type':'PLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'plcy', 'type':'PLONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserFillWindow': {'code': 0x1089, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWndPaint', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWndPaint1', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hBrush', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiExtCreateRegion': {'code': 0x108A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'px', 'type':'LPXFORM', 'in': True, 'out': False, 'optional': True},
			{'name': 'cj', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'prgndata', 'type':'LPRGNDATA', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiComputeXformCoefficients': {'code': 0x108B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetWindowsHookEx': {'code': 0x108C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Mod', 'type':'HINSTANCE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ModuleName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadId', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'HookId', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'HookProc', 'type':'HOOKPROC', 'in': True, 'out': False, 'optional': False},
			{'name': 'Ansi', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserNotifyProcessCreate': {'code': 0x108D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'NewProcessId', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ParentThreadId', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'CreateFlags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiUnrealizeObject': {'code': 0x108E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hgdiobj', 'type':'HGDIOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetTitleBarInfo': {'code': 0x108F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'pti', 'type':'PTITLEBARINFO', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiRectangle': {'code': 0x1090, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xLeft', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yTop', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xRight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yBottom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetThreadDesktop': {'code': 0x1091, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDesktop', 'type':'HDESK', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetDCEx': {'code': 0x1092, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hRegion', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetScrollBarInfo': {'code': 0x1093, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'idObject', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'psbi', 'type':'PSCROLLBARINFO', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetTextExtent': {'code': 0x1094, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpwsz', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cwc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'psize', 'type':'LPSIZE', 'in': True, 'out': False, 'optional': False},
			{'name': 'flOpts', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetWindowFNID': {'code': 0x1095, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'fnID', 'type':'WORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetLayout': {'code': 0x1096, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'wox', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwLayout', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCalcMenuBar': {'code': 0x1097, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'width', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'prc', 'type':'LPRECT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserThunkedMenuItemInfo': {'code': 0x1098, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'uItem', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'fByPosition', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'bInsert', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpmii', 'type':'LPMENUITEMINFOW', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpszCaption', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiExcludeClipRect': {'code': 0x1099, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xLeft', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yTop', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xRight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yBottom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateDIBSection': {'code': 0x109A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hSectionApp', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'dwOffset', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbmi', 'type':'LPBITMAPINFO', 'in': True, 'out': False, 'optional': True},
			{'name': 'iUsage', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjHeader', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'fl', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwColorSpace', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppvBits', 'type':'PPVOID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetDCforBitmap': {'code': 0x109B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hsurf', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDestroyCursor': {'code': 0x109C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Handle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'bForce', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDestroyWindow': {'code': 0x109D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Wnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCallHwndParam': {'code': 0x109E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Param', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Routine', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateDIBitmapInternal': {'code': 0x109F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'cx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'fInit', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjInit', 'type':'LPBYTE', 'in': True, 'out': False, 'optional': True},
			{'name': 'pbmi', 'type':'LPBITMAPINFO', 'in': True, 'out': False, 'optional': True},
			{'name': 'iUsage', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjMaxInitInfo', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjMaxBits', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'f', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'hcmXform', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserOpenWindowStation': {'code': 0x10A0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwDesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetCursorIconData': {'code': 0x10A1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hCursor', 'type':'HCURSOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'pustrModule', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'puSrcName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': True},
			{'name': 'pCursorData', 'type':'PCURSORDATA', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCloseDesktop': {'code': 0x10A2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDesktop', 'type':'HDESK', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserOpenDesktop': {'code': 0x10A3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwDesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetProcessWindowStation': {'code': 0x10A4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWindowStation', 'type':'HWINSTA', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetAtomName': {'code': 0x10A5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'atom', 'type':'ATOM', 'in': True, 'out': False, 'optional': False},
			{'name': 'pustrName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiExtCreatePen': {'code': 0x10A6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'flPenStyle', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ulWidth', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'iBrushStyle', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ulColor', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'lClientHatch', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'lHatch', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cstyle', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pulStyle', 'type':'PULONG', 'in': True, 'out': False, 'optional': True},
			{'name': 'cjDIB', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'bOldStylePen', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbrush', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': True},
		]},

	'NtGdiCreatePaletteInternal': {'code': 0x10A7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pLogPal', 'type':'LPLOGPALETTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'cEntries', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetBrushOrg': {'code': 0x10A8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptOut', 'type':'LPPOINT', 'in': False, 'out': True, 'optional': True},
		]},

	'NtUserBuildNameList': {'code': 0x10A9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWinSta', 'type':'HWINSTA', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'pRequiredSize', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetPixel': {'code': 0x10AA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdcDst', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'crColor', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRegisterClassExWOW': {'code': 0x10AB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpwcx', 'type':'LPWNDCLASSEXW', 'in': True, 'out': False, 'optional': False},
			{'name': 'pustrClassName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'pustrCVersion', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'pClassMenuName', 'type':'PCLSMENUNAME', 'in': True, 'out': False, 'optional': False},
			{'name': 'fnID', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pWow', 'type':'LPDWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreatePatternBrushInternal': {'code': 0x10AC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'bPen', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'b8X8', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetAncestor': {'code': 0x10AD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetOutlineTextMetricsInternalW': {'code': 0x10AE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'Data', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'otm', 'type':'POUTLINETEXTMETRICW', 'in': True, 'out': False, 'optional': False},
			{'name': 'Tmd', 'type':'PTMDIFF', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetBitmapBits': {'code': 0x10AF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'cj', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjInit', 'type':'PBYTE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCloseWindowStation': {'code': 0x10B0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWinSta', 'type':'HWINSTA', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetDoubleClickTime': {'code': 0x10B1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserEnableScrollBar': {'code': 0x10B2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'wSBflags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'wArrows', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateSolidBrush': {'code': 0x10B3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'cr', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbr', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': True},
		]},

	#TODO: Unknown parameter types
	'NtUserGetClassInfoEx': {'code': 0x10B4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateClientObj': {'code': 0x10B5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ulType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUnregisterClass': {'code': 0x10B6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ClassNameOrAtom', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'hInstance', 'type':'HINSTANCE', 'in': True, 'out': False, 'optional': False},
			{'name': 'pClassMenuName', 'type':'PCLSMENUNAME', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDeleteMenu': {'code': 0x10B7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'uPosition', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uFlags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiRectInRegion': {'code': 0x10B8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hrgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'prcl', 'type':'LPRECT', 'in': True, 'out': True, 'optional': False},
		]},

	'NtUserScrollWindowEx': {'code': 0x10B9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'dx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'rect', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'clipRect', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgnUpdate', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'rcUpdate', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'flags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetPixel': {'code': 0x10BA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetClassLong': {'code': 0x10BB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Offset', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwNewLong', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'Ansi', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetMenuBarInfo': {'code': 0x10BC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'idObject', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'idItem', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pmbi', 'type':'PMENUBARINFO', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetNearestPaletteIndex': {'code': 0x10BD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hpal', 'type':'HPALETTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'crColor', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetCharWidthW': {'code': 0x10BE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'wcFirst', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cwc', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwc', 'type':'PWCHAR', 'in': True, 'out': False, 'optional': True},
			{'name': 'fl', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvBuf', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtUserInvalidateRgn': {'code': 0x10BF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hRgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'bErase', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetClipboardOwner': {'code': 0x10C0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserSetWindowRgn': {'code': 0x10C1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hRgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'bRedraw', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserBitBltSysBmp': {'code': 0x10C2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'nXDest', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nYDest', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nWidth', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nHeight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nXSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nYSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwRop', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetCharWidthInfo': {'code': 0x10C3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pChWidthInfo', 'type':'PCHWIDTHINFO', 'in': False, 'out': True, 'optional': False},
		]},

	'NtUserValidateRect': {'code': 0x10C4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpRect', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCloseClipboard': {'code': 0x10C5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserOpenClipboard': {'code': 0x10C6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetClipboardData': {'code': 0x10C7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'fmt', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hMem', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'scd', 'type':'PSETCLIPBDATA', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserEnableMenuItem': {'code': 0x10C8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'uIDEnableItem', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uEnable', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserAlterWindowStyle': {'code': 0x10C9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Index', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewValue', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFillRgn': {'code': 0x10CA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbrush', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetWindowPlacement': {'code': 0x10CB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpwndpl', 'type':'PWINDOWPLACEMENT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiModifyWorldTransform': {'code': 0x10CC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxformUnsafe', 'type':'LPXFORM', 'in': True, 'out': False, 'optional': True},
			{'name': 'dwMode', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetFontData': {'code': 0x10CD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'Table', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Offset', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'LPVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'Size', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetOpenClipboardWindow': {'code': 0x10CE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserSetThreadState': {'code': 0x10CF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiOpenDCW': {'code': 0x10D0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
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

	'NtUserTrackMouseEvent': {'code': 0x10D1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpEventTrack', 'type':'LPTRACKMOUSEEVENT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetTransform': {'code': 0x10D2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'iXform', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pXForm', 'type':'LPXFORM', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDestroyMenu': {'code': 0x10D3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetBitmapBits': {'code': 0x10D4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hBitmap', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjBuffer', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pUnsafeBits', 'type':'PBYTE', 'in': False, 'out': True, 'optional': True},
		]},

	'NtUserConsoleControl': {'code': 0x10D5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ConsoleCtrl', 'type':'CONSOLECONTROL', 'in': True, 'out': False, 'optional': False},
			{'name': 'ConsoleCtrlInfo', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ConsoleCtrlInfoLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetActiveWindow': {'code': 0x10D6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Wnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetInformationThread': {'code': 0x10D7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformationClass', 'type':'USERTHREADINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetWindowPlacement': {'code': 0x10D8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpwndpl', 'type':'PWINDOWPLACEMENT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetControlColor': {'code': 0x10D9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwndParent', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'CtlMsg', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetMetaRgn': {'code': 0x10DA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetMiterLimit': {'code': 0x10DB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwNew', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdwOut', 'type':'PDWORD', 'in': True, 'out': True, 'optional': True},
		]},

	'NtGdiSetVirtualResolution': {'code': 0x10DC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxVirtualDevicePixel', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cyVirtualDevicePixel', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxVirtualDeviceMm', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cyVirtualDeviceMm', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetRasterizerCaps': {'code': 0x10DD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'praststat', 'type':'LPRASTERIZER_STATUS', 'in': False, 'out': True, 'optional': False},
			{'name': 'cjBytes', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetWindowWord': {'code': 0x10DE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Index', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'NewVal', 'type':'WORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetClipboardFormatName': {'code': 0x10DF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'uFormat', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpszFormatName', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cchMaxCount', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRealInternalGetMessage': {'code': 0x10E0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpMsg', 'type':'LPMSG', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'wMsgFilterMin', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'wMsgFilterMax', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'wRemoveMsg', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'bGMSG', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCreateLocalMemHandle': {'code': 0x10E1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMem', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'pData', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'cbData', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcbData', 'type':'PDWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserAttachThreadInput': {'code': 0x10E2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'idAttach', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'idAttachTo', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'fAttach', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateHalftonePalette': {'code': 0x10E3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserPaintMenuBar': {'code': 0x10E4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'left', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'right', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'top', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'bActive', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetKeyboardState': {'code': 0x10E5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpKeyState', 'type':'LPBYTE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCombineTransform': {'code': 0x10E6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pxfDst', 'type':'LPXFORM', 'in': False, 'out': True, 'optional': False},
			{'name': 'pxfSrc1', 'type':'LPXFORM', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxfSrc2', 'type':'LPXFORM', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCreateAcceleratorTable': {'code': 0x10E7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Entries', 'type':'LPACCEL', 'in': True, 'out': False, 'optional': False},
			{'name': 'EntriesCount', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetCursorFrameInfo': {'code': 0x10E8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hCursor', 'type':'HCURSOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'istep', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'rate_jiffies', 'type':'PINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'num_steps', 'type':'PDWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetAltTabInfo': {'code': 0x10E9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'iItem', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pati', 'type':'PALTTABINFO', 'in': True, 'out': False, 'optional': False},
			{'name': 'pszItemText', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cchItemText', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'Ansi', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetCaretBlinkTime': {'code': 0x10EA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiQueryFontAssocInfo': {'code': 0x10EB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserProcessConnect': {'code': 0x10EC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserEnumDisplayDevices': {'code': 0x10ED, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpDevice', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'iDevNum', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpDisplayDevice', 'type':'PDISPLAY_DEVICEW', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserEmptyClipboard': {'code': 0x10EE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserGetClipboardData': {'code': 0x10EF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'fmt', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pgcd', 'type':'PGETCLIPBDATA', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRemoveMenu': {'code': 0x10F0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'uPosition', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uFlags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetBoundsRect': {'code': 0x10F1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'prc', 'type':'LPRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'f', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetBitmapDimension': {'code': 0x10F2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hBitmap', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'psizDim', 'type':'LPSIZE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtUserConvertMemHandle': {'code': 0x10F3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pData', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'cbData', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDestroyAcceleratorTable': {'code': 0x10F4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Table', 'type':'HACCEL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetGUIThreadInfo': {'code': 0x10F5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'idThread', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpgui', 'type':'LPGUITHREADINFO', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCloseFigure': {'code': 0x10F6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetWindowsHookAW': {'code': 0x10F7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'idHook', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpfn', 'type':'HOOKPROC', 'in': True, 'out': False, 'optional': False},
			{'name': 'Ansi', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetMenuDefaultItem': {'code': 0x10F8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'uItem', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'fByPos', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCheckMenuItem': {'code': 0x10F9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hmenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'uIDCheckItem', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uCheck', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetWinEventHook': {'code': 0x10FA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'eventMin', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'eventMax', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hmodWinEventProc', 'type':'HMODULE', 'in': True, 'out': False, 'optional': False},
			{'name': 'puString', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpfnWinEventProc', 'type':'WINEVENTPROC', 'in': True, 'out': False, 'optional': False},
			{'name': 'idProcess', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'idThread', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwflags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUnhookWinEvent': {'code': 0x10FB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWinEventHook', 'type':'HWINEVENTHOOK', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserLockWindowUpdate': {'code': 0x10FC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetSystemMenu': {'code': 0x10FD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserThunkedMenuInfo': {'code': 0x10FE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpcmi', 'type':'LPCMENUINFO', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiBeginPath': {'code': 0x10FF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEndPath': {'code': 0x1100, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFillPath': {'code': 0x1101, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCallHwnd': {'code': 0x1102, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Routine', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDdeInitialize': {'code': 0x1103, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserModifyUserStartupInfoFlags': {'code': 0x1104, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCountClipboardFormats': {'code': 0x1105, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiAddFontMemResourceEx': {'code': 0x1106, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pvBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjBuffer', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdv', 'type':'PDESIGNVECTOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjDV', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pNumFonts', 'type':'PDWORD', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiEqualRgn': {'code': 0x1107, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hrgn1', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgn2', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetSystemPaletteUse': {'code': 0x1108, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiRemoveFontMemResourceEx': {'code': 0x1109, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMMFont', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserEnumDisplaySettings': {'code': 0x110A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpszDeviceName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'iModeNum', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpDevMode', 'type':'LPDEVMODEW', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserPaintDesktop': {'code': 0x110B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiExtEscape': {'code': 0x110C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': True},
			{'name': 'pDriver', 'type':'PWCHAR', 'in': True, 'out': False, 'optional': True},
			{'name': 'cwcDriver', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'iEsc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjIn', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjIn', 'type':'LPSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'cjOut', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjOut', 'type':'LPSTR', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiSetBitmapDimension': {'code': 0x110D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'cx', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cy', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'psizeOut', 'type':'LPSIZE', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiSetFontEnumeration': {'code': 0x110E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ulType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserChangeClipboardChain': {'code': 0x110F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWndRemove', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWndNewNext', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetClipboardViewer': {'code': 0x1110, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWndNewViewer', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserShowWindowAsync': {'code': 0x1111, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'nCmdShow', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateColorSpace': {'code': 0x1112, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pLogColorSpace', 'type':'PLOGCOLORSPACEEXW', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiDeleteColorSpace': {'code': 0x1113, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hColorSpace', 'type':'HCOLORSPACE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserActivateKeyboardLayout': {'code': 0x1114, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hKl', 'type':'HKL', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtBindCompositionSurface': {'code': 0x1115, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtCloseCompositionInputSink': {'code': 0x1116, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtCompositionInputThread': {'code': 0x1117, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtCompositionSetDropTarget': {'code': 0x1118, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtCreateCompositionInputSink': {'code': 0x1119, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtCreateCompositionSurfaceHandle': {'code': 0x111A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'desiredAccess', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'securityAttributes', 'type':'PSECURITY_ATTRIBUTES', 'in': True, 'out': False, 'optional': True},
			{'name': 'surfaceHandle', 'type':'PHANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtCreateImplicitCompositionInputSink': {'code': 0x111B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionAddCrossDeviceVisualChild': {'code': 0x111C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionBeginFrame': {'code': 0x111D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionCommitChannel': {'code': 0x111E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtDCompositionCommitSynchronizationObject': {'code': 0x111F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtDCompositionConfirmFrame': {'code': 0x1120, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionConnectPipe': {'code': 0x1121, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionCreateAndBindSharedSection': {'code': 0x1122, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionCreateChannel': {'code': 0x1123, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionCreateConnection': {'code': 0x1124, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionCreateDwmChannel': {'code': 0x1125, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtDCompositionCreateSharedVisualHandle': {'code': 0x1126, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtDCompositionCreateSynchronizationObject': {'code': 0x1127, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtDCompositionDestroyChannel': {'code': 0x1128, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionDestroyConnection': {'code': 0x1129, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionDiscardFrame': {'code': 0x112A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionDuplicateHandleToProcess': {'code': 0x112B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionDuplicateSwapchainHandleToDwm': {'code': 0x112C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtDCompositionEnableDDASupport': {'code': 0x112D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtDCompositionEnableMMCSS': {'code': 0x112E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtDCompositionGetBatchId': {'code': 0x112F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtDCompositionGetChannels': {'code': 0x1130, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionGetConnectionBatch': {'code': 0x1131, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionGetDeletedResources': {'code': 0x1132, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionGetFrameLegacyTokens': {'code': 0x1133, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionGetFrameStatistics': {'code': 0x1134, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionGetFrameSurfaceUpdates': {'code': 0x1135, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionProcessChannelBatchBuffer': {'code': 0x1136, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionReferenceSharedResourceOnDwmChannel': {'code': 0x1137, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionRegisterThumbnailVisual': {'code': 0x1138, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
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

	#TODO: Unknown parameter types
	'NtDCompositionRegisterVirtualDesktopVisual': {'code': 0x1139, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionReleaseAllResources': {'code': 0x113A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionRemoveCrossDeviceVisualChild': {'code': 0x113B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionRetireFrame': {'code': 0x113C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionSetChannelCallbackId': {'code': 0x113D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionSetChannelCommitCompletionEvent': {'code': 0x113E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtDCompositionSetChildRootVisual': {'code': 0x113F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtDCompositionSetDebugCounter': {'code': 0x1140, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionSubmitDWMBatch': {'code': 0x1141, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtDCompositionSuspendAnimations': {'code': 0x1142, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtDCompositionSynchronize': {'code': 0x1143, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionTelemetryAnimationScenarioBegin': {'code': 0x1144, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionTelemetryAnimationScenarioReference': {'code': 0x1145, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionTelemetryAnimationScenarioUnreference': {'code': 0x1146, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionTelemetrySetApplicationId': {'code': 0x1147, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionTelemetryTouchInteractionBegin': {'code': 0x1148, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionTelemetryTouchInteractionEnd': {'code': 0x1149, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionTelemetryTouchInteractionUpdate': {'code': 0x114A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionUpdatePointerCapture': {'code': 0x114B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDCompositionWaitForChannel': {'code': 0x114C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtDWMBindCursorToOutputConfig': {'code': 0x114D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtDWMCommitInputSystemOutputConfig': {'code': 0x114E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtDWMSetCursorOrientation': {'code': 0x114F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtDWMSetInputSystemOutputConfig': {'code': 0x1150, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtDesktopCaptureBits': {'code': 0x1151, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtDuplicateCompositionInputSink': {'code': 0x1152, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtDxgkGetProcessList': {'code': 0x1153, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtDxgkRegisterVailProcess': {'code': 0x1154, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtDxgkSubmitPresentBltToHwQueue': {'code': 0x1155, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtDxgkVailConnect': {'code': 0x1156, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtDxgkVailDisconnect': {'code': 0x1157, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtDxgkVailPromoteCompositionSurface': {'code': 0x1158, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtEnableOneCoreTransformMode': {'code': 0x1159, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectAddContent': {'code': 0x115A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectAddPoolBuffer': {'code': 0x115B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectConsumerAcquirePresent': {'code': 0x115C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectConsumerAdjustUsageReference': {'code': 0x115D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectConsumerBeginProcessPresent': {'code': 0x115E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectConsumerEndProcessPresent': {'code': 0x115F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectConsumerPostMessage': {'code': 0x1160, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectConsumerQueryBufferInfo': {'code': 0x1161, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectCreate': {'code': 0x1162, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectDisconnectEndpoint': {'code': 0x1163, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectOpen': {'code': 0x1164, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectQueryBufferAvailableEvent': {'code': 0x1165, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectQueryEndpointConnected': {'code': 0x1166, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectQueryNextMessageToProducer': {'code': 0x1167, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectReadNextMessageToProducer': {'code': 0x1168, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectRemoveContent': {'code': 0x1169, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectRemovePoolBuffer': {'code': 0x116A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtFlipObjectSetContent': {'code': 0x116B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtGdiAbortDoc': {'code': 0x116C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiAbortPath': {'code': 0x116D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiAddEmbFontToDC': {'code': 0x116E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pFontID', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiAddFontResourceW': {'code': 0x116F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pwszFiles', 'type':'PWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cwc', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cFiles', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'f', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwPidTid', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdv', 'type':'PDESIGNVECTOR', 'in': True, 'out': False, 'optional': True},
		]},

	#TODO: Unknown function until now
	'NtGdiAddInitialFonts': {'code': 0x1170, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtGdiAddRemoteFontToDC': {'code': 0x1171, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjBuffer', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pufi', 'type':'PUNIVERSAL_FONT_ID', 'in': True, 'out': False, 'optional': True},
		]},

	'NtGdiAddRemoteMMInstanceToDC': {'code': 0x1172, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pddv', 'type':'LPDOWNLOADDESIGNVECTOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjDDV', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiAngleArc': {'code': 0x1173, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwRadius', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwStartAngle', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwSweepAngle', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiAnyLinkedFonts': {'code': 0x1174, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiArcInternal': {'code': 0x1175, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'arctype', 'type':'ARCTYPE', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x1', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y1', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'x2', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y2', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'x3', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y3', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'x4', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y4', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiBRUSHOBJ_DeleteRbrush': {'code': 0x1176, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': True},
			{'name': 'pboB', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': True},
		]},

	'NtGdiBRUSHOBJ_hGetColorTransform': {'code': 0x1177, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiBRUSHOBJ_pvAllocRbrush': {'code': 0x1178, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'cj', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiBRUSHOBJ_pvGetRbrush': {'code': 0x1179, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiBRUSHOBJ_ulGetBrushColor': {'code': 0x117A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiBeginGdiRendering': {'code': 0x117B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'bDiscard', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'KernelModeDeviceHandle', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCLIPOBJ_bEnum': {'code': 0x117C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'cj', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pul', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiCLIPOBJ_cEnumStart': {'code': 0x117D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'bAll', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'iType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'iDirection', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cLimit', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCLIPOBJ_ppoGetPath': {'code': 0x117E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCancelDC': {'code': 0x117F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiChangeGhostFont': {'code': 0x1180, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfontID', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'bLoad', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCheckBitmapBits': {'code': 0x1181, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hColorTransform', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvBits', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'bmFormat', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwWidth', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwHeight', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwStride', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'paResults', 'type':'PBYTE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiClearBitmapAttributes': {'code': 0x1182, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiClearBrushAttributes': {'code': 0x1183, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiColorCorrectPalette': {'code': 0x1184, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hpal', 'type':'HPALETTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'uFirstEntry', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cPalEntries', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppalEntry', 'type':'PPALETTEENTRY', 'in': True, 'out': True, 'optional': False},
			{'name': 'uCommand', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiConfigureOPMProtectedOutput': {'code': 0x1185, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiConvertMetafileRect': {'code': 0x1186, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'prect', 'type':'PRECTL', 'in': True, 'out': True, 'optional': False},
		]},

	'NtGdiCreateBitmapFromDxSurface': {'code': 0x1187, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'uiWidth', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uiHeight', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'Format', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'hDxSharedSurface', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtGdiCreateBitmapFromDxSurface2': {'code': 0x1188, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'uiWidth', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uiHeight', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'Format', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'SubresourceIndex', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'bSharedSurfaceNtHandle', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'hDxSharedSurface', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
		]},

	'NtGdiCreateColorTransform': {'code': 0x1189, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pLogColorSpaceW', 'type':'LPLOGCOLORSPACEW', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvSrcProfile', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'cjSrcProfile', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvDestProfile', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'cjDestProfile', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvTargetProfile', 'type':'PVOID', 'in': True, 'out': False, 'optional': True},
			{'name': 'cjTargetProfile', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateEllipticRgn': {'code': 0x118A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'xLeft', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yTop', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xRight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yBottom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateHatchBrushInternal': {'code': 0x118B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ulStyle', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'clrr', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
			{'name': 'bPen', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateMetafileDC': {'code': 0x118C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiCreateOPMProtectedOutput': {'code': 0x118D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiCreateOPMProtectedOutputs': {'code': 0x118E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateRoundRectRgn': {'code': 0x118F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'xLeft', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yTop', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xRight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yBottom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xWidth', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yHeight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateServerMetaFile': {'code': 0x1190, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'iType', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjData', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjData', 'type':'LPBYTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'mm', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'xExt', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'yExt', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiCreateSessionMappedDIBSection': {'code': 0x1191, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': True},
			{'name': 'hSectionApp', 'type':'HANDLE', 'in': True, 'out': False, 'optional': True},
			{'name': 'dwOffset', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbmi', 'type':'LPBITMAPINFO', 'in': True, 'out': False, 'optional': True},
			{'name': 'iUsage', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjHeader', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'fl', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwColorSpace', 'type':'ULONG_PTR', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDDCCIGetCapabilitiesString': {'code': 0x1192, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDDCCIGetCapabilitiesStringLength': {'code': 0x1193, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDDCCIGetTimingReport': {'code': 0x1194, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDDCCIGetVCPFeature': {'code': 0x1195, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDDCCISaveCurrentSettings': {'code': 0x1196, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDDCCISetVCPFeature': {'code': 0x1197, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdCreateFullscreenSprite': {'code': 0x1198, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIAbandonSwapChain': {'code': 0x1199, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIAcquireKeyedMutex': {'code': 0x119A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIAcquireKeyedMutex2': {'code': 0x119B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIAcquireSwapChain': {'code': 0x119C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIAddSurfaceToSwapChain': {'code': 0x119D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIAdjustFullscreenGamma': {'code': 0x119E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICacheHybridQueryValue': {'code': 0x119F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIChangeVideoMemoryReservation': {'code': 0x11A0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiDdDDICheckExclusiveOwnership': {'code': 0x11A1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICheckMonitorPowerState': {'code': 0x11A2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICheckMultiPlaneOverlaySupport': {'code': 0x11A3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICheckMultiPlaneOverlaySupport2': {'code': 0x11A4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICheckMultiPlaneOverlaySupport3': {'code': 0x11A5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICheckOcclusion': {'code': 0x11A6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICheckSharedResourceAccess': {'code': 0x11A7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICheckVidPnExclusiveOwnership': {'code': 0x11A8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICloseAdapter': {'code': 0x11A9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIConfigureSharedResource': {'code': 0x11AA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateAllocation': {'code': 0x11AB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDICreateBundleObject': {'code': 0x11AC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateContext': {'code': 0x11AD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateContextVirtual': {'code': 0x11AE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateDCFromMemory': {'code': 0x11AF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateDevice': {'code': 0x11B0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDICreateHwContext': {'code': 0x11B1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDICreateHwQueue': {'code': 0x11B2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateKeyedMutex': {'code': 0x11B3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateKeyedMutex2': {'code': 0x11B4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateOutputDupl': {'code': 0x11B5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateOverlay': {'code': 0x11B6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreatePagingQueue': {'code': 0x11B7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDICreateProtectedSession': {'code': 0x11B8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateSwapChain': {'code': 0x11B9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDICreateSynchronizationObject': {'code': 0x11BA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIDDisplayEnum': {'code': 0x11BB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroyAllocation': {'code': 0x11BC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroyAllocation2': {'code': 0x11BD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroyContext': {'code': 0x11BE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroyDCFromMemory': {'code': 0x11BF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroyDevice': {'code': 0x11C0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIDestroyHwContext': {'code': 0x11C1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIDestroyHwQueue': {'code': 0x11C2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroyKeyedMutex': {'code': 0x11C3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroyOutputDupl': {'code': 0x11C4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroyOverlay': {'code': 0x11C5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroyPagingQueue': {'code': 0x11C6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIDestroyProtectedSession': {'code': 0x11C7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIDestroySynchronizationObject': {'code': 0x11C8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIDispMgrCreate': {'code': 0x11C9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level':3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIDispMgrSourceOperation': {'code': 0x11CA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIDispMgrTargetOperation': {'code': 0x11CB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIEnumAdapters': {'code': 0x11CC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIEnumAdapters2': {'code': 0x11CD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIEscape': {'code': 0x11CE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIEvict': {'code': 0x11CF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIExtractBundleObject': {'code': 0x11D0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIFlipOverlay': {'code': 0x11D1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIFlushHeapTransitions': {'code': 0x11D2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIFreeGpuVirtualAddress': {'code': 0x11D3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIGetAllocationPriority': {'code': 0x11D4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetCachedHybridQueryValue': {'code': 0x11D5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetContextInProcessSchedulingPriority': {'code': 0x11D6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetContextSchedulingPriority': {'code': 0x11D7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetDWMVerticalBlankEvent': {'code': 0x11D8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetDeviceState': {'code': 0x11D9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetDisplayModeList': {'code': 0x11DA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIGetMemoryBudgetTarget': {'code': 0x11DB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIGetMultiPlaneOverlayCaps': {'code': 0x11DC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetMultisampleMethodList': {'code': 0x11DD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetOverlayState': {'code': 0x11DE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIGetPostCompositionCaps': {'code': 0x11DF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetPresentHistory': {'code': 0x11E0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetPresentQueueEvent': {'code': 0x11E1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIGetProcessDeviceRemovalSupport': {'code': 0x11E2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIGetProcessSchedulingPriorityBand': {'code': 0x11E3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetProcessSchedulingPriorityClass': {'code': 0x11E4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetResourcePresentPrivateDriverData': {'code': 0x11E5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetRuntimeData': {'code': 0x11E6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetScanLine': {'code': 0x11E7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetSetSwapChainMetadata': {'code': 0x11E8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetSharedPrimaryHandle': {'code': 0x11E9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIGetSharedResourceAdapterLuid': {'code': 0x11EA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIGetYieldPercentage': {'code': 0x11EB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIInvalidateActiveVidPn': {'code': 0x11EC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIInvalidateCache': {'code': 0x11ED, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDILock': {'code': 0x11EE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDILock2': {'code': 0x11EF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIMakeResident': {'code': 0x11F0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIMapGpuVirtualAddress': {'code': 0x11F1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIMarkDeviceAsError': {'code': 0x11F2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDINetDispGetNextChunkInfo': {'code': 0x11F3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDINetDispQueryMiracastDisplayDeviceStatus': {'code': 0x11F4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDINetDispQueryMiracastDisplayDeviceSupport': {'code': 0x11F5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDINetDispStartMiracastDisplayDevice': {'code': 0x11F6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDINetDispStopMiracastDisplayDevice': {'code': 0x11F7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDINetDispStopSessions': {'code': 0x11F8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOfferAllocations': {'code': 0x11F9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenAdapterFromDeviceName': {'code': 0x11FA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenAdapterFromHdc': {'code': 0x11FB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenAdapterFromLuid': {'code': 0x11FC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIOpenBundleObjectNtHandleFromName': {'code': 0x11FD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenKeyedMutex': {'code': 0x11FE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenKeyedMutex2': {'code': 0x11FF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIOpenKeyedMutexFromNtHandle': {'code': 0x1200, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenNtHandleFromName': {'code': 0x1201, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIOpenProtectedSessionFromNtHandle': {'code': 0x1202, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenResource': {'code': 0x1203, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenResourceFromNtHandle': {'code': 0x1204, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenSwapChain': {'code': 0x1205, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenSyncObjectFromNtHandle': {'code': 0x1206, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenSyncObjectFromNtHandle2': {'code': 0x1207, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenSyncObjectNtHandleFromName': {'code': 0x1208, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOpenSynchronizationObject': {'code': 0x1209, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOutputDuplGetFrameInfo': {'code': 0x120A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOutputDuplGetMetaData': {'code': 0x120B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOutputDuplGetPointerShapeData': {'code': 0x120C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOutputDuplPresent': {'code': 0x120D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIOutputDuplReleaseFrame': {'code': 0x120E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level':2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIPinDirectFlipResources': {'code': 0x120F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIPollDisplayChildren': {'code': 0x1210, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIPresent': {'code': 0x1211, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIPresentMultiPlaneOverlay': {'code': 0x1212, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIPresentMultiPlaneOverlay2': {'code': 0x1213, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIPresentMultiPlaneOverlay3': {'code': 0x1214, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIPresentRedirected': {'code': 0x1215, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryAdapterInfo': {'code': 0x1216, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryAllocationResidency': {'code': 0x1217, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryClockCalibration': {'code': 0x1218, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryFSEBlock': {'code': 0x1219, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryProcessOfferInfo': {'code': 0x121A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIQueryProtectedSessionInfoFromNtHandle': {'code': 0x121B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIQueryProtectedSessionStatus': {'code': 0x121C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryRemoteVidPnSourceFromGdiDisplayName': {'code': 0x121D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryResourceInfo': {'code': 0x121E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryResourceInfoFromNtHandle': {'code': 0x121F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 12,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryStatistics': {'code': 0x1220, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryVidPnExclusiveOwnership': {'code': 0x1221, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIQueryVideoMemoryInfo': {'code': 0x1222, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIReclaimAllocations': {'code': 0x1223, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIReclaimAllocations2': {'code': 0x1224, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIReleaseKeyedMutex': {'code': 0x1225, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIReleaseKeyedMutex2': {'code': 0x1226, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIReleaseProcessVidPnSourceOwners': {'code': 0x1227, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIReleaseSwapChain': {'code': 0x1228, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIRemoveSurfaceFromSwapChain': {'code': 0x1229, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIRender': {'code': 0x122A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIReserveGpuVirtualAddress': {'code': 0x122B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetAllocationPriority': {'code': 0x122C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetContextInProcessSchedulingPriority': {'code': 0x122D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetContextSchedulingPriority': {'code': 0x122E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetDisplayMode': {'code': 0x122F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetDisplayPrivateDriverFormat': {'code': 0x1230, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetDodIndirectSwapchain': {'code': 0x1231, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetFSEBlock': {'code': 0x1232, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetGammaRamp': {'code': 0x1233, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetHwProtectionTeardownRecovery': {'code': 0x1234, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level':2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDISetMemoryBudgetTarget': {'code': 0x1235, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDISetMonitorColorSpaceTransform': {'code': 0x1236, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDISetProcessDeviceRemovalSupport': {'code': 0x1237, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level':3,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDISetProcessSchedulingPriorityBand': {'code': 0x1238, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetProcessSchedulingPriorityClass': {'code': 0x1239, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetQueuedLimit': {'code': 0x123A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetStablePowerState': {'code': 0x123B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetStereoEnabled': {'code': 0x123C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetSyncRefreshCountWaitTarget': {'code': 0x123D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetVidPnSourceHwProtection': {'code': 0x123E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISetVidPnSourceOwner': {'code': 0x123F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDISetYieldPercentage': {'code': 0x1240, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIShareObjects': {'code': 0x1241, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISharedPrimaryLockNotification': {'code': 0x1242, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISharedPrimaryUnLockNotification': {'code': 0x1243, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISignalSynchronizationObject': {'code': 0x1244, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISignalSynchronizationObjectFromCpu': {'code': 0x1245, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISignalSynchronizationObjectFromGpu': {'code': 0x1246, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISignalSynchronizationObjectFromGpu2': {'code': 0x1247, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDISubmitCommand': {'code': 0x1248, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDISubmitCommandToHwQueue': {'code': 0x1249, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDISubmitSignalSyncObjectsToHwQueue': {'code': 0x124A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDISubmitWaitForSyncObjectsToHwQueue': {'code': 0x124B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDITrimProcessCommitment': {'code': 0x124C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiDdDDIUnOrderedPresentSwapChain': {'code': 0x124D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIUnlock': {'code': 0x124E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIUnlock2': {'code': 0x124F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIUnpinDirectFlipResources': {'code': 0x1250, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIUpdateAllocationProperty': {'code': 0x1251, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIUpdateGpuVirtualAddress': {'code': 0x1252, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIUpdateOverlay': {'code': 0x1253, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIWaitForIdle': {'code': 0x1254, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIWaitForSynchronizationObject': {'code': 0x1255, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIWaitForSynchronizationObjectFromCpu': {'code': 0x1256, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIWaitForSynchronizationObjectFromGpu': {'code': 0x1257, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIWaitForVerticalBlankEvent': {'code': 0x1258, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDDIWaitForVerticalBlankEvent2': {'code': 0x1259, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdDestroyFullscreenSprite': {'code': 0x125A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDdNotifyFullscreenSpriteUpdate': {'code': 0x125B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiDdQueryVisRgnUniqueness': {'code': 0x125C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiDeleteColorTransform': {'code': 0x125D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hColorTransform', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDescribePixelFormat': {'code': 0x125E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDestroyOPMProtectedOutput': {'code': 0x125F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiDestroyPhysicalMonitor': {'code': 0x1260, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiDoBanding': {'code': 0x1261, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'bStart', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptl', 'type':'PPOINT', 'in': False, 'out': True, 'optional': False},
			{'name': 'pSize', 'type':'PSIZE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiDrawEscape': {'code': 0x1262, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'iEsc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjIn', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjIn', 'type':'LPSTR', 'in': True, 'out': False, 'optional': True},
		]},

	'NtGdiDwmCreatedBitmapRemotingOutput': {'code': 0x1263, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiEllipse': {'code': 0x1264, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xLeft', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yTop', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xRight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yBottom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEnableEudc': {'code': 0x1265, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'b', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEndDoc': {'code': 0x1266, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEndGdiRendering': {'code': 0x1267, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'bDiscard', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbDeviceRemoved', 'type':'PBOOL', 'in': False, 'out': True, 'optional': False},
			{'name': 'KernelModeDeviceHandle', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEndPage': {'code': 0x1268, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngAlphaBlend': {'code': 0x1269, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'psoDest', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoSrc', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclDest', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclSrc', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pBlendObj', 'type':'PBLENDOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngAssociateSurface': {'code': 0x126A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hsurf', 'type':'HSURF', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdev', 'type':'HDEV', 'in': True, 'out': False, 'optional': False},
			{'name': 'flHooks', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngBitBlt': {'code': 0x126B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'psoTrg', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoSrc', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoMask', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclTrg', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlSrc', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlMask', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlBrush', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'rop4', 'type':'ROP4', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngCheckAbort': {'code': 0x126C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngComputeGlyphSet': {'code': 0x126D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'nCodePage', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nFirstChar', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cChars', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngCopyBits': {'code': 0x126E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'psoDst', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoSrc', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclDst', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlSrc', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiEngCreateBitmap': {'code': 0x126F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngCreateClip': {'code': 0x1270, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiEngCreateDeviceBitmap': {'code': 0x1271, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiEngCreateDeviceSurface': {'code': 0x1272, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngCreatePalette': {'code': 0x1273, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'iMode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cColors', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pulColors', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'flRed', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'flGreen', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'flBlue', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngDeleteClip': {'code': 0x1274, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngDeletePalette': {'code': 0x1275, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hPal', 'type':'HPALETTE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngDeletePath': {'code': 0x1276, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ppo', 'type':'PPATHOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngDeleteSurface': {'code': 0x1277, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hsurf', 'type':'HSURF', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngEraseSurface': {'code': 0x1278, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'prcl', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'iColor', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngFillPath': {'code': 0x1279, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppo', 'type':'PPATHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlBrushOrg', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'mix', 'type':'MIX', 'in': True, 'out': False, 'optional': False},
			{'name': 'flOptions', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngGradientFill': {'code': 0x127A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'psoDest', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pVertex', 'type':'PTRIVERTEX', 'in': True, 'out': False, 'optional': False},
			{'name': 'nVertex', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pMesh', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'nMesh', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclExtents', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlDitherOrg', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'ulMode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngLineTo': {'code': 0x127B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'x1', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'y1', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'x2', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'y2', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclBounds', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'mix', 'type':'MIX', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngLockSurface': {'code': 0x127C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hsurf', 'type':'HSURF', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngMarkBandingSurface': {'code': 0x127D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hsurf', 'type':'HSURF', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngPaint': {'code': 0x127E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlBrushOrg', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'mix', 'type':'MIX', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngPlgBlt': {'code': 0x127F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'psoTrg', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoSrc', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoMsk', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': True},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': True},
			{'name': 'pca', 'type':'PCOLORADJUSTMENT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlBrushOrg', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptfx', 'type':'PPOINTFIX', 'in': True, 'out': False, 'optional': False},
			{'name': 'prcl', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptl', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': True},
			{'name': 'iMode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngStretchBlt': {'code': 0x1280, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'psoDest', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoSrc', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoMask', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': True},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': True},
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': True},
			{'name': 'pca', 'type':'PCOLORADJUSTMENT', 'in': True, 'out': False, 'optional': True},
			{'name': 'pptlHTOrg', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclDest', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclSrc', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlMask', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': True},
			{'name': 'iMode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngStretchBltROP': {'code': 0x1281, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'psoTrg', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoSrc', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoMask', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pca', 'type':'PCOLORADJUSTMENT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlBrushOrg', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclTrg', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclSrc', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlMask', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'iMode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'rop4', 'type':'ROP4', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngStrokeAndFillPath': {'code': 0x1282, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppo', 'type':'PPATHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxo', 'type':'PXFORMOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pboStroke', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'plineattrs', 'type':'PLINEATTRS', 'in': True, 'out': False, 'optional': False},
			{'name': 'pboFill', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlBrushOrg', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'mix', 'type':'MIX', 'in': True, 'out': False, 'optional': False},
			{'name': 'flOptions', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngStrokePath': {'code': 0x1283, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppo', 'type':'PPATHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxo', 'type':'PXFORMOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbo', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlBrushOrg', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'plineattrs', 'type':'PLINEATTRS', 'in': True, 'out': False, 'optional': False},
			{'name': 'mix', 'type':'MIX', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngTextOut': {'code': 0x1284, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pstro', 'type':'PSTROBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pfo', 'type':'PFONTOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclExtra', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclOpaque', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'pboFore', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pboOpaque', 'type':'PBRUSHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlOrg', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'mix', 'type':'MIX', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngTransparentBlt': {'code': 0x1285, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'psoDst', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'psoSrc', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclDst', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'prclSrc', 'type':'PRECTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'iTransColor', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ulReserved', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiEngUnlockSurface': {'code': 0x1286, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiEnsureDpiDepDefaultGuiFontForPlateau': {'code': 0x1287, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtGdiEnumFonts': {'code': 0x1288, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'iEnumType', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'flWin31Compat', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cchFaceName', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwszFaceName', 'type':'LPCWSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'lfCharSet', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pulCount', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'pvUserModeBuffer', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiEnumObjects': {'code': 0x1289, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'iObjectType', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjBuf', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvBuf', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiEudcLoadUnloadLink': {'code': 0x128A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pBaseFaceName', 'type':'LPCWSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'cwcBaseFaceName', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pEudcFontPath', 'type':'LPCWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cwcEudcFontPath', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'iPriority', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'iFontLinkType', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'bLoadLin', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiExtFloodFill': {'code': 0x128B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'crColor', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
			{'name': 'iFillType', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFONTOBJ_cGetAllGlyphHandles': {'code': 0x128C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfo', 'type':'PFONTOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'phg', 'type':'PHGLYPH', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiFONTOBJ_cGetGlyphs': {'code': 0x128D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfo', 'type':'PFONTOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'iMode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cGlyph', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'phg', 'type':'PHGLYPH', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppvGlyph', 'type':'PPVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFONTOBJ_pQueryGlyphAttrs': {'code': 0x128E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfo', 'type':'PFONTOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'iMode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFONTOBJ_pfdg': {'code': 0x128F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfo', 'type':'PFONTOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFONTOBJ_pifi': {'code': 0x1290, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfo', 'type':'PFONTOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFONTOBJ_pvTrueTypeFontFile': {'code': 0x1291, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfo', 'type':'PFONTOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcjFile', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiFONTOBJ_pxoGetXform': {'code': 0x1292, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfo', 'type':'PFONTOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFONTOBJ_vGetInfo': {'code': 0x1293, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfo', 'type':'PFONTOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pfi', 'type':'PFONTINFO', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFlattenPath': {'code': 0x1294, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFontIsLinked': {'code': 0x1295, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiForceUFIMapping': {'code': 0x1296, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pufi', 'type':'PUNIVERSAL_FONT_ID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFrameRgn': {'code': 0x1297, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hrgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbrush', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
			{'name': 'xWidth', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yHeight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiFullscreenControl': {'code': 0x1298, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'FullscreenCommand', 'type':'FULLSCREENCONTROL', 'in': True, 'out': False, 'optional': False},
			{'name': 'FullscreenInput', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'FullscreenInputLength', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'FullscreenOutput', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'FullscreenOutputLength', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiGetAppliedDeviceGammaRamp': {'code': 0x1299, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiGetBitmapDpiScaleValue': {'code': 0x129A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtGdiGetBoundsRect': {'code': 0x129B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'prc', 'type':'LPRECT', 'in': False, 'out': True, 'optional': False},
			{'name': 'flags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetCOPPCompatibleOPMInformation': {'code': 0x129C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetCertificate': {'code': 0x129D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetCertificateByHandle': {'code': 0x129E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetCertificateSize': {'code': 0x129F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetCertificateSizeByHandle': {'code': 0x12A0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetCharABCWidthsW': {'code': 0x12A1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'wchFirst', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cwch', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwch', 'type':'PWCHAR', 'in': True, 'out': False, 'optional': True},
			{'name': 'fl', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvBuf', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetCharacterPlacementW': {'code': 0x12A2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwsz', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'nCount', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nMaxExtent', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pgcpw', 'type':'LPGCP_RESULTSW', 'in': True, 'out': True, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetColorAdjustment': {'code': 0x12A3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcaOut', 'type':'PCOLORADJUSTMENT', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetColorSpaceforBitmap': {'code': 0x12A4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hsurf', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetCurrentDpiInfo': {'code': 0x12A5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hmon', 'type':'HMONITOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvStruct', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiGetDCDpiScaleValue': {'code': 0x12A6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtGdiGetDeviceCaps': {'code': 0x12A7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'i', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetDeviceCapsAll': {'code': 0x12A8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pDevCaps', 'type':'PDEVCAPS', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetDeviceGammaRamp': {'code': 0x12A9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpGammaRamp', 'type':'LPVOID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetDeviceWidth': {'code': 0x12AA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetDhpdev': {'code': 0x12AB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdev', 'type':'HDEV', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetETM': {'code': 0x12AC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'petm', 'type':'PEXTTEXTMETRIC', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiGetEmbUFI': {'code': 0x12AD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pufi', 'type':'PUNIVERSAL_FONT_ID', 'in': False, 'out': True, 'optional': False},
			{'name': 'pdv', 'type':'PDESIGNVECTOR', 'in': False, 'out': True, 'optional': True},
			{'name': 'pcjDV', 'type':'PLONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'pulBaseCheckSum', 'type':'PLONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'pfl', 'type':'PFLONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'embFontID', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetEmbedFonts': {'code': 0x12AE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtGdiGetEntry': {'code': 0x12AF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetEudcTimeStampEx': {'code': 0x12B0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpBaseFaceName', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'cwcBaseFaceName', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'bSystemTimeStamp', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetFontFileData': {'code': 0x12B1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'uFileCollectionID', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uFileIndex', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pullFileOffset', 'type':'PLARGE_INTEGER', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvBuf', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'cjBuf', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetFontFileInfo': {'code': 0x12B2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'uFileCollectionID', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uFileIndex', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pffi', 'type':'PFONT_FILE_INFO', 'in': False, 'out': True, 'optional': True},
			{'name': 'cjSize', 'type':'SIZE_T', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcjActualSize', 'type':'PSIZE_T', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetFontResourceInfoInternalW': {'code': 0x12B3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pwszFiles', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cwc', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cFiles', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjBuf', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdwBytes', 'type':'LPDWORD', 'in': False, 'out': True, 'optional': False},
			{'name': 'pvBuf', 'type':'LPVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'iType', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetFontUnicodeRanges': {'code': 0x12B4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pgs', 'type':'LPGLYPHSET', 'in': False, 'out': True, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiGetGammaRampCapability': {'code': 0x12B5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtGdiGetGlyphIndicesW': {'code': 0x12B6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwc', 'type':'LPCWSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'cwc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pgi', 'type':'LPWORD', 'in': False, 'out': True, 'optional': True},
			{'name': 'iMode', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetGlyphIndicesWInternal': {'code': 0x12B7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwc', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'cwc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pgi', 'type':'LPWORD', 'in': False, 'out': True, 'optional': True},
			{'name': 'iMode', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'bSubset', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetGlyphOutline': {'code': 0x12B8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'wch', 'type':'WCHAR', 'in': True, 'out': False, 'optional': False},
			{'name': 'iFormat', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pgm', 'type':'LPGLYPHMETRICS', 'in': False, 'out': True, 'optional': False},
			{'name': 'cjBuf', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'UnsafeBuf', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'pmat2', 'type':'LPMAT2', 'in': True, 'out': False, 'optional': False},
			{'name': 'bIgnoreRotation', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetKerningPairs': {'code': 0x12B9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'cPairs', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pkpDst', 'type':'PKERNINGPAIR', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiGetLinkedUFIs': {'code': 0x12BA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pufiLinkedUFIs', 'type':'PUNIVERSAL_FONT_ID', 'in': False, 'out': True, 'optional': True},
			{'name': 'cBufferSize', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetMiterLimit': {'code': 0x12BB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetMonitorID': {'code': 0x12BC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjSize', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pszMonitorID', 'type':'LPWSTR', 'in': False, 'out': True, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetNumberOfPhysicalMonitors': {'code': 0x12BD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetOPMInformation': {'code': 0x12BE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetOPMRandomNumber': {'code': 0x12BF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetObjectBitmapHandle': {'code': 0x12C0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbr', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
			{'name': 'piUsage', 'type':'PUINT', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetPath': {'code': 0x12C1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlBuf', 'type':'LPPOINT', 'in': False, 'out': True, 'optional': True},
			{'name': 'pjTypes', 'type':'LPBYTE', 'in': False, 'out': True, 'optional': True},
			{'name': 'cptBuf', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetPerBandInfo': {'code': 0x12C2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppbi', 'type':'PPERBANDINFO', 'in': True, 'out': True, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetPhysicalMonitorDescription': {'code': 0x12C3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetPhysicalMonitors': {'code': 0x12C4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetProcessSessionFonts': {'code': 0x12C5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetPublicFontTableChangeCookie': {'code': 0x12C6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiGetRealizationInfo': {'code': 0x12C7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pri', 'type':'PFONT_REALIZATION_INFO', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetServerMetaFileBits': {'code': 0x12C8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hmo', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjData', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjData', 'type':'LPBYTE', 'in': False, 'out': True, 'optional': True},
			{'name': 'piType', 'type':'PDWORD', 'in': False, 'out': True, 'optional': False},
			{'name': 'pmm', 'type':'PDWORD', 'in': False, 'out': True, 'optional': False},
			{'name': 'pxExt', 'type':'PDWORD', 'in': False, 'out': True, 'optional': False},
			{'name': 'pyExt', 'type':'PDWORD', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetSpoolMessage': {'code': 0x12C9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'u1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'u2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'u3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'u4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetStats': {'code': 0x12CA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hProcess', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'iIndex', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'iPidType', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pResults', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'cjResultSize', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetStringBitmapW': {'code': 0x12CB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwsz', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cwc', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpSB', 'type':'PBYTE', 'in': False, 'out': True, 'optional': False},
			{'name': 'cj', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiGetSuggestedOPMProtectedOutputArraySize': {'code': 0x12CC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetTextExtentExW': {'code': 0x12CD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'UnsafeString', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': True},
			{'name': 'Count', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'MaxExtent', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'UnsafeFit', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'UnsafeDx', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'UnsafeSize', 'type':'LPSIZE', 'in': False, 'out': True, 'optional': False},
			{'name': 'fl', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiGetUFI': {'code': 0x12CE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pufi', 'type':'PUNIVERSAL_FONT_ID', 'in': False, 'out': True, 'optional': False},
			{'name': 'pdv', 'type':'PDESIGNVECTOR', 'in': False, 'out': True, 'optional': True},
			{'name': 'pcjDV', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'pulBaseCheckSum', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'pfl', 'type':'PFLONG', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiGetUFIPathname': {'code': 0x12CF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pufi', 'type':'PUNIVERSAL_FONT_ID', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcwc', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'pwszPathname', 'type':'LPWSTR', 'in': False, 'out': True, 'optional': True},
			{'name': 'pcNumFiles', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'fl', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbMemFont', 'type':'PBOOL', 'in': False, 'out': True, 'optional': True},
			{'name': 'pcjView', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
			{'name': 'pvView', 'type':'PVOID', 'in': False, 'out': True, 'optional': True},
			{'name': 'pbTTC', 'type':'PBOOL', 'in': False, 'out': True, 'optional': True},
			{'name': 'piTTC', 'type':'PULONG', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiGradientFill': {'code': 0x12D0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pVertex', 'type':'PTRIVERTEX', 'in': True, 'out': False, 'optional': False},
			{'name': 'nVertex', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pMesh', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'nMesh', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ulMode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiHLSurfGetInformation': {'code': 0x12D1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hlsurf', 'type':'HLSURF', 'in': True, 'out': False, 'optional': False},
			{'name': 'InformationClass', 'type':'HLSURF_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvInfoBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjInfoBuffer', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiHLSurfSetInformation': {'code': 0x12D2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hlsurf', 'type':'HLSURF', 'in': True, 'out': False, 'optional': False},
			{'name': 'InformationClass', 'type':'HLSURF_INFORMATION_CLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvInfoBuffer', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjInfoBuffer', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiHT_Get8BPPFormatPalette': {'code': 0x12D3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pPaletteEntry', 'type':'LPPALETTEENTRY', 'in': False, 'out': True, 'optional': True},
			{'name': 'RedGamma', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
			{'name': 'GreenGamma', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
			{'name': 'BlueGamma', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiHT_Get8BPPMaskPalette': {'code': 0x12D4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pPaletteEntry', 'type':'LPPALETTEENTRY', 'in': False, 'out': True, 'optional': True},
			{'name': 'Use8BPPMaskPal', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'CMYMask', 'type':'BYTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'RedGamma', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
			{'name': 'GreenGamma', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
			{'name': 'BlueGamma', 'type':'USHORT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiIcmBrushInfo': {'code': 0x12D5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbrush', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbmiDIB', 'type':'LPBITMAPINFO', 'in': True, 'out': True, 'optional': False},
			{'name': 'pvBits', 'type':'PVOID', 'in': True, 'out': True, 'optional': False},
			{'name': 'pulBits', 'type':'PULONG', 'in': True, 'out': True, 'optional': False},
			{'name': 'piUsage', 'type':'PDWORD', 'in': False, 'out': True, 'optional': True},
			{'name': 'pbAlreadyTran', 'type':'PBOOL', 'in': False, 'out': True, 'optional': True},
			{'name': 'Command', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiInit': {'code': 0x12D6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiInitSpool': {'code': 0x12D7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtGdiMakeFontDir': {'code': 0x12D8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'flEmbed', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjFontDir', 'type':'PBYTE', 'in': False, 'out': True, 'optional': False},
			{'name': 'cjFontDir', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pwszPathname', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cjPathname', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiMakeInfoDC': {'code': 0x12D9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'bSet', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiMakeObjectUnXferable': {'code': 0x12DA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'h', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiMakeObjectXferable': {'code': 0x12DB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'h', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwProcessId', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiMirrorWindowOrg': {'code': 0x12DC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiMonoBitmap': {'code': 0x12DD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiMoveTo': {'code': 0x12DE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiOffsetClipRgn': {'code': 0x12DF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPATHOBJ_bEnum': {'code': 0x12E0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ppo', 'type':'PPATHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppd', 'type':'PPATHDATA', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiPATHOBJ_bEnumClipLines': {'code': 0x12E1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ppo', 'type':'PPATHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'cb', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcl', 'type':'PCLIPLINE', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiPATHOBJ_vEnumStart': {'code': 0x12E2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ppo', 'type':'PPATHOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPATHOBJ_vEnumStartClipLines': {'code': 0x12E3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ppo', 'type':'PPATHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pco', 'type':'PCLIPOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pso', 'type':'PSURFOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pla', 'type':'PLINEATTRS', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPATHOBJ_vGetBounds': {'code': 0x12E4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ppo', 'type':'PPATHOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'prectfx', 'type':'PRECTFX', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiPathToRegion': {'code': 0x12E5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPlgBlt': {'code': 0x12E6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdcTrg', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptlTrg', 'type':'LPPOINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdcSrc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'ySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbmMask', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': True},
			{'name': 'xMask', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yMask', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'crBackColor', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPolyDraw': {'code': 0x12E7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'ppt', 'type':'LPPOINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pjAttr', 'type':'LPBYTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'cpt', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPolyTextOutW': {'code': 0x12E8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptw', 'type':'PPOLYTEXTW', 'in': True, 'out': False, 'optional': False},
			{'name': 'cStr', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwCodePage', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPtInRegion': {'code': 0x12E9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hrgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiPtVisible': {'code': 0x12EA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiQueryFonts': {'code': 0x12EB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pufiFontList', 'type':'PUNIVERSAL_FONT_ID', 'in': False, 'out': True, 'optional': False},
			{'name': 'nBufferSize', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pTimeStamp', 'type':'PLARGE_INTEGER', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiRemoveFontResourceW': {'code': 0x12EC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pwszFiles', 'type':'LPCWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cwc', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cFiles', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'fl', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwPidTid', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdv', 'type':'PDESIGNVECTOR', 'in': True, 'out': False, 'optional': True},
		]},

	'NtGdiRemoveMergeFont': {'code': 0x12ED, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pufi', 'type':'PUNIVERSAL_FONT_ID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiResetDC': {'code': 0x12EE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdm', 'type':'LPDEVMODEW', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbBanding', 'type':'PBOOL', 'in': False, 'out': True, 'optional': False},
			{'name': 'pDriverInfo2', 'type':'PDRIVER_INFO_2W', 'in': True, 'out': False, 'optional': True},
			{'name': 'ppUMdhpdev', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiResizePalette': {'code': 0x12EF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hpal', 'type':'HPALETTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'cEntry', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiRoundRect': {'code': 0x12F0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'x1', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y1', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'x2', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y2', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'x3', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y3', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSTROBJ_bEnum': {'code': 0x12F1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pstro', 'type':'PSTROBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pc', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'ppgpos', 'type':'PPGLYPHPOS', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiSTROBJ_bEnumPositionsOnly': {'code': 0x12F2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pstro', 'type':'PSTROBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pc', 'type':'PULONG', 'in': False, 'out': True, 'optional': False},
			{'name': 'ppgpos', 'type':'PPGLYPHPOS', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiSTROBJ_bGetAdvanceWidths': {'code': 0x12F3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pstro', 'type':'PSTROBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'iFirst', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'c', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptqD', 'type':'PPOINTQF', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiSTROBJ_dwGetCodePage': {'code': 0x12F4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pstro', 'type':'PSTROBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSTROBJ_vEnumStart': {'code': 0x12F5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pstro', 'type':'PSTROBJ', 'in': True, 'out': True, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiScaleRgn': {'code': 0x12F6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtGdiScaleValues': {'code': 0x12F7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtGdiScaleViewportExtEx': {'code': 0x12F8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xNum', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xDenom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yNum', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yDenom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pszOut', 'type':'LPSIZE', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiScaleWindowExtEx': {'code': 0x12F9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xNum', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xDenom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yNum', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yDenom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pszOut', 'type':'LPSIZE', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiSelectBrush': {'code': 0x12FA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hbrush', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSelectClipPath': {'code': 0x12FB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'iMode', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSelectPen': {'code': 0x12FC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hpen', 'type':'HPEN', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetBitmapAttributes': {'code': 0x12FD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBITMAP', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetBrushAttributes': {'code': 0x12FE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hbm', 'type':'HBRUSH', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetColorAdjustment': {'code': 0x12FF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pca', 'type':'PCOLORADJUSTMENT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetColorSpace': {'code': 0x1300, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'hColorSpace', 'type':'HCOLORSPACE', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetDeviceGammaRamp': {'code': 0x1301, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpGammaRamp', 'type':'LPVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetFontXform': {'code': 0x1302, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwxScale', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwyScale', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetIcmMode': {'code': 0x1303, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'nCommand', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'ulMode', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetLinkedUFIs': {'code': 0x1304, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pufiLinks', 'type':'PUNIVERSAL_FONT_ID', 'in': True, 'out': False, 'optional': False},
			{'name': 'uNumUFIs', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetMagicColors': {'code': 0x1305, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'peMagic', 'type':'PALETTEENTRY', 'in': True, 'out': False, 'optional': False},
			{'name': 'Index', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtGdiSetOPMSigningKeyAndSequenceNumbers': {'code': 0x1306, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetPUMPDOBJ': {'code': 0x1307, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'humpd', 'type':'HUMPD', 'in': True, 'out': False, 'optional': True},
			{'name': 'bStoreID', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'phumpd', 'type':'PHUMPD', 'in': True, 'out': True, 'optional': True},
			{'name': 'pbWOW64', 'type':'PBOOL', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiSetPixelFormat': {'code': 0x1308, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'ipfd', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtGdiSetPrivateDeviceGammaRamp': {'code': 0x1309, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtGdiSetRectRgn': {'code': 0x130A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hrgn', 'type':'HRGN', 'in': True, 'out': False, 'optional': False},
			{'name': 'xLeft', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yTop', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'xRight', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yBottom', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetSizeDevice': {'code': 0x130B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxVirtualDevice', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cyVirtualDevice', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetSystemPaletteUse': {'code': 0x130C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'ui', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetTextJustification': {'code': 0x130D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'lBreakExtra', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cBreak', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSetUMPDSandboxState': {'code': 0x130E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'bEnabled', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiStartDoc': {'code': 0x130F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdi', 'type':'LPDOCINFOW', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbBanding', 'type':'PBOOL', 'in': False, 'out': True, 'optional': False},
			{'name': 'iJob', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiStartPage': {'code': 0x1310, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiStrokeAndFillPath': {'code': 0x1311, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiStrokePath': {'code': 0x1312, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiSwapBuffers': {'code': 0x1313, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiTransparentBlt': {'code': 0x1314, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdcDst', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'yDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cyDst', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdcSrc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'xSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'ySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cxSrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cySrc', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'TransColor', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiUMPDEngFreeUserMem': {'code': 0x1315, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ppv', 'type':'PPVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiUnloadPrinterDriver': {'code': 0x1316, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pDriverName', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'cbDriverName', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiUnmapMemFont': {'code': 0x1317, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pvView', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiUpdateColors': {'code': 0x1318, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiUpdateTransform': {'code': 0x1319, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hdc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiWidenPath': {'code': 0x131A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiXFORMOBJ_bApplyXform': {'code': 0x131B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'None', 'type':'PXFORMOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PPOINTL', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PPOINTL', 'in': False, 'out': True, 'optional': False},
		]},

	'NtGdiXFORMOBJ_iGetXform': {'code': 0x131C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pxo', 'type':'PXFORMOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'pxform', 'type':'PXFORML', 'in': False, 'out': True, 'optional': True},
		]},

	'NtGdiXLATEOBJ_cGetPalette': {'code': 0x131D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'iPal', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'cPal', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pPal', 'type':'PULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiXLATEOBJ_hGetColorTransform': {'code': 0x131E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': False},
		]},

	'NtGdiXLATEOBJ_iXlate': {'code': 0x131F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pxlo', 'type':'PXLATEOBJ', 'in': True, 'out': False, 'optional': False},
			{'name': 'iColor', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtHWCursorUpdatePointer': {'code': 0x1320, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtIsOneCoreTransformMode': {'code': 0x1321, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITActivateInputProcessing': {'code': 0x1322, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITBindInputTypeToMonitors': {'code': 0x1323, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITCoreMsgKGetConnectionHandle': {'code': 0x1324, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITCoreMsgKOpenConnectionTo': {'code': 0x1325, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITCoreMsgKSend': {'code': 0x1326, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITDeactivateInputProcessing': {'code': 0x1327, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITDisableMouseIntercept': {'code': 0x1328, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITDispatchCompletion': {'code': 0x1329, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITEnableMouseIntercept': {'code': 0x132A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITGetCursorUpdateHandle': {'code': 0x132B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITSetInputCallbacks': {'code': 0x132C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITSetInputDelegationMode': {'code': 0x132D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITSetLastInputRecipient': {'code': 0x132E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITSynthesizeMouseInput': {'code': 0x132F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITSynthesizeMouseWheel': {'code': 0x1330, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITSynthesizeTouchInput': {'code': 0x1331, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITUpdateInputGlobals': {'code': 0x1332, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMITWaitForMultipleObjectsEx': {'code': 0x1333, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtMapVisualRelativePoints': {'code': 0x1334, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtNotifyPresentToCompositionSurface': {'code': 0x1335, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtOpenCompositionSurfaceDirtyRegion': {'code': 0x1336, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtOpenCompositionSurfaceSectionInfo': {'code': 0x1337, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtOpenCompositionSurfaceSwapChainHandleInfo': {'code': 0x1338, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQueryCompositionInputIsImplicit': {'code': 0x1339, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQueryCompositionInputQueueAndTransform': {'code': 0x133A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQueryCompositionInputSink': {'code': 0x133B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQueryCompositionInputSinkLuid': {'code': 0x133C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQueryCompositionInputSinkViewId': {'code': 0x133D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQueryCompositionSurfaceBinding': {'code': 0x133E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQueryCompositionSurfaceHDRMetaData': {'code': 0x133F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQueryCompositionSurfaceRenderingRealization': {'code': 0x1340, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtQueryCompositionSurfaceStatistics': {'code': 0x1341, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtRIMAddInputObserver': {'code': 0x1342, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
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
	'NtRIMAreSiblingDevices': {'code': 0x1343, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMDeviceIoControl': {'code': 0x1344, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMEnableMonitorMappingForDevice': {'code': 0x1345, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMFreeInputBuffer': {'code': 0x1346, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMGetDevicePreparsedData': {'code': 0x1347, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtRIMGetDevicePreparsedDataLockfree': {'code': 0x1348, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtRIMGetDeviceProperties': {'code': 0x1349, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMGetDevicePropertiesLockfree': {'code': 0x134A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMGetPhysicalDeviceRect': {'code': 0x134B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMGetSourceProcessId': {'code': 0x134C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtRIMObserveNextInput': {'code': 0x134D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtRIMOnPnpNotification': {'code': 0x134E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMOnTimerNotification': {'code': 0x134F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMReadInput': {'code': 0x1350, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMRegisterForInput': {'code': 0x1351, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtRIMRemoveInputObserver': {'code': 0x1352, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtRIMSetTestModeStatus': {'code': 0x1353, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtRIMUnregisterForInput': {'code': 0x1354, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtRIMUpdateInputObserverRegistration': {'code': 0x1355, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtSetCompositionSurfaceAnalogExclusive': {'code': 0x1356, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtSetCompositionSurfaceBufferUsage': {'code': 0x1357, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtSetCompositionSurfaceDirectFlipState': {'code': 0x1358, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtSetCompositionSurfaceIndependentFlipInfo': {'code': 0x1359, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtSetCompositionSurfaceStatistics': {'code': 0x135A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtTokenManagerConfirmOutstandingAnalogToken': {'code': 0x135B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtTokenManagerCreateCompositionTokenHandle': {'code': 0x135C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtTokenManagerCreateFlipObjectReturnTokenHandle': {'code': 0x135D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtTokenManagerCreateFlipObjectTokenHandle': {'code': 0x135E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtTokenManagerGetAnalogExclusiveSurfaceUpdates': {'code': 0x135F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtTokenManagerGetAnalogExclusiveTokenEvent': {'code': 0x1360, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtTokenManagerOpenSectionAndEvents': {'code': 0x1361, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtTokenManagerThread': {'code': 0x1362, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUnBindCompositionSurface': {'code': 0x1363, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUpdateInputSinkTransforms': {'code': 0x1364, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserAcquireIAMKey': {'code': 0x1365, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserAcquireInteractiveControlBackgroundAccess': {'code': 0x1366, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserAddClipboardFormatListener': {'code': 0x1367, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserAssociateInputContext': {'code': 0x1368, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserAutoPromoteMouseInPointer': {'code': 0x1369, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserAutoRotateScreen': {'code': 0x136A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserBeginLayoutUpdate': {'code': 0x136B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserBlockInput': {'code': 0x136C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'BlockIt', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserBroadcastThemeChangeEvent': {'code': 0x136D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserBuildHimcList': {'code': 0x136E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserBuildPropList': {'code': 0x136F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Buffer', 'type':'LPVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'BufferSize', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Count', 'type':'PDWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserCalculatePopupWindowPosition': {'code': 0x1370, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCallHwndOpt': {'code': 0x1371, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'Routine', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserCanBrokerForceForeground': {'code': 0x1372, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserChangeDisplaySettings': {'code': 0x1373, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpszDeviceName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpDevMode', 'type':'LPDEVMODEW', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwflags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'lParam', 'type':'LPVOID', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserChangeWindowMessageFilterEx': {'code': 0x1374, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserCheckAccessForIntegrityLevel': {'code': 0x1375, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserCheckProcessForClipboardAccess': {'code': 0x1376, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserCheckProcessSession': {'code': 0x1377, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserCheckWindowThreadDesktop': {'code': 0x1378, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserChildWindowFromPointEx': {'code': 0x1379, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Parent', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserClearForeground': {'code': 0x137A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserClipCursor': {'code': 0x137B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpRect', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserCompositionInputSinkLuidFromPoint': {'code': 0x137C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserCompositionInputSinkViewInstanceIdFromPoint': {'code': 0x137D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserConfirmResizeCommit': {'code': 0x137E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserCreateDCompositionHwndTarget': {'code': 0x137F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserCreateDesktopEx': {'code': 0x1380, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserCreateEmptyCursorObject': {'code': 0x1381, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserCreateInputContext': {'code': 0x1382, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserCreatePalmRejectionDelayZone': {'code': 0x1383, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserCreateWindowGroup': {'code': 0x1384, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserCreateWindowStation': {'code': 0x1385, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ObjectAttributes', 'type':'POBJECT_ATTRIBUTES', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwDesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown5', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown6', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserCtxDisplayIOCtl': {'code': 0x1386, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserDeferWindowPosAndBand': {'code': 0x1387, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
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
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserDelegateCapturePointers': {'code': 0x1388, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserDelegateInput': {'code': 0x1389, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserDeleteWindowGroup': {'code': 0x138A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserDestroyDCompositionHwndTarget': {'code': 0x138B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDestroyInputContext': {'code': 0x138C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserDestroyPalmRejectionDelayZone': {'code': 0x138D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserDisableImmersiveOwner': {'code': 0x138E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDisableProcessWindowFiltering': {'code': 0x138F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserDisableThreadIme': {'code': 0x1390, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserDiscardPointerFrameMessages': {'code': 0x1391, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserDisplayConfigGetDeviceInfo': {'code': 0x1392, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserDisplayConfigSetDeviceInfo': {'code': 0x1393, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDoSoundConnect': {'code': 0x1394, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserDoSoundDisconnect': {'code': 0x1395, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserDragDetect': {'code': 0x1396, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'pointX', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pointY', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDragObject': {'code': 0x1397, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd1', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hwnd2', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'u1', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'dw1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'hc1', 'type':'HCURSOR', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDrawAnimatedRects': {'code': 0x1398, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'idAni', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lprcFrom', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lprcTo', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDrawCaption': {'code': 0x1399, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hDc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpRc', 'type':'LPCRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uFlags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDrawCaptionTemp': {'code': 0x139A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hDC', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpRc', 'type':'LPCRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hFont', 'type':'HFONT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hIcon', 'type':'HICON', 'in': True, 'out': False, 'optional': False},
			{'name': 'str', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'uFlags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDrawMenuBarTemp': {'code': 0x139B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'None', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'HFONT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserDwmGetRemoteSessionOcclusionEvent': {'code': 0x139C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserDwmGetRemoteSessionOcclusionState': {'code': 0x139D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserDwmKernelShutdown': {'code': 0x139E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserDwmKernelStartup': {'code': 0x139F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserDwmValidateWindow': {'code': 0x13A0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserEnableChildWindowDpiMessage': {'code': 0x13A1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserEnableIAMAccess': {'code': 0x13A2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserEnableMouseInPointer': {'code': 0x13A3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserEnableMouseInputForCursorSuppression': {'code': 0x13A4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserEnableNonClientDpiScaling': {'code': 0x13A5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserEnableResizeLayoutSynchronization': {'code': 0x13A6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserEnableSoftwareCursorForScreenCapture': {'code': 0x13A7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserEnableTouchPad': {'code': 0x13A8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserEnableWindowGDIScaledDpiMessage': {'code': 0x13A9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserEnableWindowGroupPolicy': {'code': 0x13AA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserEnableWindowResizeOptimization': {'code': 0x13AB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserEndMenu': {'code': 0x13AC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserEvent': {'code': 0x13AD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserFlashWindowEx': {'code': 0x13AE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfwi', 'type':'PFLASHWINFO', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserFrostCrashedWindow': {'code': 0x13AF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserFunctionalizeDisplayConfig': {'code': 0x13B0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserGetActiveProcessesDpis': {'code': 0x13B1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserGetAppImeLevel': {'code': 0x13B2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetAutoRotationState': {'code': 0x13B3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetCIMSSM': {'code': 0x13B4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetCaretPos': {'code': 0x13B5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpPoint', 'type':'LPPOINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetClipCursor': {'code': 0x13B6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpRect', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetClipboardAccessToken': {'code': 0x13B7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetClipboardViewer': {'code': 0x13B8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserGetComboBoxInfo': {'code': 0x13B9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcbi', 'type':'PCOMBOBOXINFO', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetCurrentInputMessageSource': {'code': 0x13BA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserGetCursor': {'code': 0x13BB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserGetCursorDims': {'code': 0x13BC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetCursorInfo': {'code': 0x13BD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pci', 'type':'PCURSORINFO', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetDManipHookInitFunction': {'code': 0x13BE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetDesktopID': {'code': 0x13BF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetDisplayAutoRotationPreferences': {'code': 0x13C0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetDisplayAutoRotationPreferencesByProcessId': {'code': 0x13C1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetDisplayConfigBufferSizes': {'code': 0x13C2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserGetDpiForCurrentProcess': {'code': 0x13C3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserGetDpiForMonitor': {'code': 0x13C4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetGestureConfig': {'code': 0x13C5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetGestureExtArgs': {'code': 0x13C6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetGestureInfo': {'code': 0x13C7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetGuiResources': {'code': 0x13C8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hProcess', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'uiFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserGetHDevName': {'code': 0x13C9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserGetHimetricScaleFactorFromPixelLocation': {'code': 0x13CA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetImeHotKey': {'code': 0x13CB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetImeInfoEx': {'code': 0x13CC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pImeInfoEx', 'type':'PIMEINFOEX', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetInputLocaleInfo': {'code': 0x13CD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetInteractiveControlDeviceInfo': {'code': 0x13CE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetInteractiveControlInfo': {'code': 0x13CF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserGetInteractiveCtrlSupportedWaveforms': {'code': 0x13D0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserGetInternalWindowPos': {'code': 0x13D1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'rectWnd', 'type':'LPRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'ptIcon', 'type':'LPPOINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetKeyNameText': {'code': 0x13D2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lParam', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpString', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
			{'name': 'nSize', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetKeyboardLayoutName': {'code': 0x13D3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpszName', 'type':'LPWSTR', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetLayeredWindowAttributes': {'code': 0x13D4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcrKey', 'type':'PCOLORREF', 'in': True, 'out': False, 'optional': False},
			{'name': 'pbAlpha', 'type':'PBYTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'pdwFlags', 'type':'PDWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetListBoxInfo': {'code': 0x13D5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetMenuIndex': {'code': 0x13D6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'hSubMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetMenuItemRect': {'code': 0x13D7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'uItem', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lprcItem', 'type':'LPRECT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserGetMonitorBrightness': {'code': 0x13D8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserGetMouseMovePointsEx': {'code': 0x13D9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'cbSize', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lppt', 'type':'LPMOUSEMOVEPOINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpptBuf', 'type':'LPMOUSEMOVEPOINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'nBufPoints', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'resolution', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserGetOemBitmapSize': {'code': 0x13DA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserGetPhysicalDeviceRect': {'code': 0x13DB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerCursorId': {'code': 0x13DC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerDevice': {'code': 0x13DD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerDeviceCursors': {'code': 0x13DE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerDeviceProperties': {'code': 0x13DF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerDeviceRects': {'code': 0x13E0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerDevices': {'code': 0x13E1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerFrameArrivalTimes': {'code': 0x13E2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerInfoList': {'code': 0x13E3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerInputTransform': {'code': 0x13E4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPointerType': {'code': 0x13E5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetPrecisionTouchPadConfiguration': {'code': 0x13E6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetPriorityClipboardFormat': {'code': 0x13E7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'paFormatPriorityList', 'type':'PUINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cFormats', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetProcessDpiAwarenessContext': {'code': 0x13E8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetProcessUIContextInformation': {'code': 0x13E9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetQueueStatusReadonly': {'code': 0x13EA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetRawInputBuffer': {'code': 0x13EB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pData', 'type':'PRAWINPUT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcbSize', 'type':'PUINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cbSizeHeader', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetRawInputData': {'code': 0x13EC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hRawInput', 'type':'HRAWINPUT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uiCommand', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pData', 'type':'LPVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcbSize', 'type':'PUINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cbSizeHeader', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetRawInputDeviceInfo': {'code': 0x13ED, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hDevice', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'uiCommand', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pData', 'type':'LPVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcbSize', 'type':'PUINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetRawInputDeviceList': {'code': 0x13EE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pRawInputDeviceList,', 'type':'PRAWINPUTDEVICELIST', 'in': True, 'out': False, 'optional': False},
			{'name': 'puiNumDevices', 'type':'PUINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cbSize', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetRawPointerDeviceData': {'code': 0x13EF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetRegisteredRawInputDevices': {'code': 0x13F0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pRawInputDevices', 'type':'PRAWINPUTDEVICE', 'in': True, 'out': False, 'optional': False},
			{'name': 'puiNumDevices', 'type':'PUINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cbSize', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserGetResizeDCompositionSynchronizationObject': {'code': 0x13F1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserGetSystemDpiForProcess': {'code': 0x13F2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserGetTopLevelWindow': {'code': 0x13F3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetTouchInputInfo': {'code': 0x13F4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetTouchValidationStatus': {'code': 0x13F5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetUpdatedClipboardFormats': {'code': 0x13F6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'lpuiFormats', 'type':'PUINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cFormats', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pcFormatsOut', 'type':'PUINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserGetWOWClass': {'code': 0x13F7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hInstance', 'type':'HINSTANCE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ClassName', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetWindowBand': {'code': 0x13F8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetWindowCompositionAttribute': {'code': 0x13F9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetWindowCompositionInfo': {'code': 0x13FA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetWindowDisplayAffinity': {'code': 0x13FB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGetWindowFeedbackSetting': {'code': 0x13FC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserGetWindowGroupId': {'code': 0x13FD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserGetWindowMinimizeRect': {'code': 0x13FE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserGetWindowProcessHandle': {'code': 0x13FF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserGetWindowRgnEx': {'code': 0x1400, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserGhostWindowFromHungWindow': {'code': 0x1401, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserHandleDelegatedInput': {'code': 0x1402, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserHardErrorControl': {'code': 0x1403, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserHidePointerContactVisualization': {'code': 0x1404, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserHiliteMenuItem': {'code': 0x1405, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'uItemHilite', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'uHilite', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserHungWindowFromGhostWindow': {'code': 0x1406, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserHwndQueryRedirectionInfo': {'code': 0x1407, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserHwndSetRedirectionInfo': {'code': 0x1408, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserImpersonateDdeClientWindow': {'code': 0x1409, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWndClient', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hWndServer', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInheritWindowMonitor': {'code': 0x140A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserInitTask': {'code': 0x140B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown5', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown6', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown7', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown8', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown9', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown10', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown11', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInitialize': {'code': 0x140C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserInitializeClientPfnArrays': {'code': 0x140D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pfnClientA', 'type':'PPFNCLIENT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pfnClientW', 'type':'PPFNCLIENT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pfnClientWorker', 'type':'PPFNCLIENTWORKER', 'in': True, 'out': False, 'optional': False},
			{'name': 'hmodUser', 'type':'HINSTANCE', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserInitializeGenericHidInjection': {'code': 0x140E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserInitializeInputDeviceInjection': {'code': 0x140F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInitializePointerDeviceInjection': {'code': 0x1410, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserInitializePointerDeviceInjectionEx': {'code': 0x1411, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserInitializeTouchInjection': {'code': 0x1412, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInjectDeviceInput': {'code': 0x1413, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserInjectGenericHidInput': {'code': 0x1414, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserInjectGesture': {'code': 0x1415, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInjectKeyboardInput': {'code': 0x1416, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInjectMouseInput': {'code': 0x1417, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInjectPointerInput': {'code': 0x1418, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInjectTouchInput': {'code': 0x1419, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInteractiveControlQueryUsage': {'code': 0x141A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserInternalGetWindowIcon': {'code': 0x141B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserIsChildWindowDpiMessageEnabled': {'code': 0x141C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserIsMouseInPointerEnabled': {'code': 0x141D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserIsMouseInputEnabled': {'code': 0x141E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserIsNonClientDpiScalingEnabled': {'code': 0x141F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserIsResizeLayoutSynchronizationEnabled': {'code': 0x1420, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserIsTopLevelWindow': {'code': 0x1421, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserIsTouchWindow': {'code': 0x1422, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserIsWindowBroadcastingDpiToChildren': {'code': 0x1423, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserIsWindowGDIScaledDpiMessageEnabled': {'code': 0x1424, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserLayoutCompleted': {'code': 0x1425, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserLinkDpiCursor': {'code': 0x1426, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserLoadKeyboardLayoutEx': {'code': 0x1427, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
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
	'NtUserLockCursor': {'code': 0x1428, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserLockWindowStation': {'code': 0x1429, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWindowStation', 'type':'HWINSTA', 'in': True, 'out': False, 'optional': False},
		]},

	#Disabled for obvious reasons
	'NtUserLockWorkStation': {'code': 0x142A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 , 'disabled': True,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserLogicalToPerMonitorDPIPhysicalPoint': {'code': 0x142B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserLogicalToPhysicalDpiPointForWindow': {'code': 0x142C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserLogicalToPhysicalPoint': {'code': 0x142D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserMNDragLeave': {'code': 0x142E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserMNDragOver': {'code': 0x142F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserMagControl': {'code': 0x1430, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserMagGetContextInformation': {'code': 0x1431, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserMagSetContextInformation': {'code': 0x1432, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserMenuItemFromPoint': {'code': 0x1433, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserMinMaximize': {'code': 0x1434, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'cmd', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'Hide', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserModifyWindowTouchCapability': {'code': 0x1435, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserMsgWaitForMultipleObjectsEx': {'code': 0x1436, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserNavigateFocus': {'code': 0x1437, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserNotifyIMEStatus': {'code': 0x1438, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserOpenInputDesktop': {'code': 0x1439, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'fInherit', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwDesiredAccess', 'type':'ACCESS_MASK', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserOpenThreadDesktop': {'code': 0x143A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserPaintMonitor': {'code': 0x143B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserPerMonitorDPIPhysicalToLogicalPoint': {'code': 0x143C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpPoint', 'type':'LPPOINT', 'in': True, 'out': True, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserPhysicalToLogicalDpiPointForWindow': {'code': 0x143D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserPhysicalToLogicalPoint': {'code': 0x143E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserPrintWindow': {'code': 0x143F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdcBlt', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'nFlags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserProcessInkFeedbackCommand': {'code': 0x1440, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserPromoteMouseInPointer': {'code': 0x1441, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserPromotePointer': {'code': 0x1442, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserQueryBSDRWindow': {'code': 0x1443, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserQueryDisplayConfig': {'code': 0x1444, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserQueryInformationThread': {'code': 0x1445, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'ThreadHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformationClass', 'type':'USERTHREADINFOCLASS', 'in': True, 'out': False, 'optional': False},
			{'name': 'ThreadInformation', 'type':'PVOID', 'in': False, 'out': True, 'optional': False},
			{'name': 'ThreadInformationLength', 'type':'ULONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserQueryInputContext': {'code': 0x1446, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'unknownA', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'unknownB', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserQuerySendMessage': {'code': 0x1447, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'unknown', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRealChildWindowFromPoint': {'code': 0x1448, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'parent', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'pointX', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'pointY', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRealWaitMessageEx': {'code': 0x1449, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwWakeMask', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'uTimeout', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterBSDRWindow': {'code': 0x144A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterDManipHook': {'code': 0x144B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterEdgy': {'code': 0x144C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterErrorReportingDialog': {'code': 0x144D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRegisterHotKey': {'code': 0x144E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'id', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'fsModifiers', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'vk', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterManipulationThread': {'code': 0x144F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterPointerDeviceNotifications': {'code': 0x1450, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterPointerInputTarget': {'code': 0x1451, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRegisterRawInputDevices': {'code': 0x1452, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pRawInputDevices', 'type':'PRAWINPUTDEVICE', 'in': True, 'out': False, 'optional': False},
			{'name': 'uiNumDevices', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'cbSize', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterServicesProcess': {'code': 0x1453, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterSessionPort': {'code': 0x1454, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterShellPTPListener': {'code': 0x1455, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRegisterTasklist': {'code': 0x1456, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterTouchHitTestingWindow': {'code': 0x1457, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRegisterTouchPadCapable': {'code': 0x1458, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRegisterUserApiHook': {'code': 0x1459, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'm_dllname1', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'm_funname1', 'type':'PUNICODE_STRING', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserReleaseDC': {'code': 0x145A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserReleaseDwmHitTestWaiters': {'code': 0x145B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserRemoteConnect': {'code': 0x145C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRemoteRedrawRectangle': {'code': 0x145D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserRemoteRedrawScreen': {'code': 0x145E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserRemoteStopScreenUpdates': {'code': 0x145F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserRemoveClipboardFormatListener': {'code': 0x1460, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserRemoveInjectionDevice': {'code': 0x1461, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserReportInertia': {'code': 0x1462, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserRequestMoveSizeOperation': {'code': 0x1463, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserResolveDesktopForWOW': {'code': 0x1464, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSendEventMessage': {'code': 0x1465, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSendInteractiveControlHapticsReport': {'code': 0x1466, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetActivationFilter': {'code': 0x1467, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetActiveProcessForMonitor': {'code': 0x1468, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetAppImeLevel': {'code': 0x1469, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetAutoRotation': {'code': 0x146A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserSetBridgeWindowChild': {'code': 0x146B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserSetBrokeredForeground': {'code': 0x146C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetCalibrationData': {'code': 0x146D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetChildWindowNoActivate': {'code': 0x146E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetClassWord': {'code': 0x146F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'nIndex', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'wNewWord', 'type':'WORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetCoreWindow': {'code': 0x1470, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetCoreWindowPartner': {'code': 0x1471, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetCursorContents': {'code': 0x1472, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Handle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'IconInfo', 'type':'PICONINFO', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserSetCursorPos': {'code': 0x1473, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserSetDesktopColorTransform': {'code': 0x1474, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserSetDialogControlDpiChangeBehavior': {'code': 0x1475, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserSetDimUndimTransitionTime': {'code': 0x1476, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserSetDisplayAutoRotationPreferences': {'code': 0x1477, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetDisplayConfig': {'code': 0x1478, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetDisplayMapping': {'code': 0x1479, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetFallbackForeground': {'code': 0x147A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetFeatureReportResponse': {'code': 0x147B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetGestureConfig': {'code': 0x147C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetImeHotKey': {'code': 0x147D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown3', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown4', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetImeInfoEx': {'code': 0x147E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'pImeInfoEx', 'type':'PIMEINFOEX', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetImeOwnerWindow': {'code': 0x147F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetInteractiveControlFocus': {'code': 0x1480, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetInteractiveCtrlRotationAngle': {'code': 0x1481, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetInternalWindowPos': {'code': 0x1482, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'showCmd', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'rect', 'type':'LPRECT', 'in': True, 'out': False, 'optional': False},
			{'name': 'pt', 'type':'LPPOINT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetLayeredWindowAttributes': {'code': 0x1483, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'crKey', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
			{'name': 'bAlpha', 'type':'BYTE', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetManipulationInputTarget': {'code': 0x1484, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetMenu': {'code': 0x1485, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'bRepaint', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetMenuContextHelpId': {'code': 0x1486, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hmenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwContextHelpId', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetMenuFlagRtoL': {'code': 0x1487, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hMenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetMirrorRendering': {'code': 0x1488, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserSetMonitorBrightness': {'code': 0x1489, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserSetObjectInformation': {'code': 0x148A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hObject', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'nIndex', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'pvInformation', 'type':'PVOID', 'in': True, 'out': False, 'optional': False},
			{'name': 'nLength', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetPrecisionTouchPadConfiguration': {'code': 0x148B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetProcessDpiAwarenessContext': {'code': 0x148C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetProcessInteractionFlags': {'code': 0x148D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetProcessRestrictionExemption': {'code': 0x148E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetProcessUIAccessZorder': {'code': 0x148F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserSetShellWindowEx': {'code': 0x1490, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwndShell', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hwndShellListView', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetSysColors': {'code': 0x1491, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'cElements', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpaElements', 'type':'PINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'lpaRgbValues', 'type':'PCOLORREF', 'in': True, 'out': False, 'optional': False},
			{'name': 'Flags', 'type':'FLONG', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetSystemCursor': {'code': 0x1492, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hcur', 'type':'HCURSOR', 'in': True, 'out': False, 'optional': False},
			{'name': 'id', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetSystemTimer': {'code': 0x1493, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserSetTargetForResourceBrokering': {'code': 0x1494, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserSetThreadInputBlocked': {'code': 0x1495, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetThreadLayoutHandles': {'code': 0x1496, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'Unknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetWindowArrangement': {'code': 0x1497, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetWindowBand': {'code': 0x1498, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetWindowCompositionAttribute': {'code': 0x1499, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetWindowCompositionTransition': {'code': 0x149A, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetWindowDisplayAffinity': {'code': 0x149B, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetWindowFeedbackSetting': {'code': 0x149C, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserSetWindowGroup': {'code': 0x149D, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserSetWindowRgnEx': {'code': 0x149E, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSetWindowShowState': {'code': 0x149F, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSetWindowStationUser': {'code': 0x14A0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWindowStation', 'type':'HWINSTA', 'in': True, 'out': False, 'optional': False},
			{'name': 'pluid', 'type':'PLUID', 'in': True, 'out': False, 'optional': False},
			{'name': 'psid', 'type':'PSID', 'in': True, 'out': False, 'optional': False},
			{'name': 'size', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserShowCursor': {'code': 0x14A1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserShowSystemCursor': {'code': 0x14A2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserShutdownBlockReasonCreate': {'code': 0x14A3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserShutdownBlockReasonQuery': {'code': 0x14A4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserShutdownReasonDestroy': {'code': 0x14A5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSignalRedirectionStartComplete': {'code': 0x14A6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserSlicerControl': {'code': 0x14A7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserSoundSentry': {'code': 0x14A8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserStopAndEndInertia': {'code': 0x14A9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserSwitchDesktop': {'code': 0x14AA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserSystemParametersInfoForDpi': {'code': 0x14AB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserTestForInteractiveUser': {'code': 0x14AC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'unknown', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserTrackPopupMenuEx': {'code': 0x14AD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hmenu', 'type':'HMENU', 'in': True, 'out': False, 'optional': False},
			{'name': 'fuFlags', 'type':'UINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'x', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'INT', 'in': True, 'out': False, 'optional': False},
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'lptpm', 'type':'LPTPMPARAMS', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserTransformPoint': {'code': 0x14AE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserTransformRect': {'code': 0x14AF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserUndelegateInput': {'code': 0x14B0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUnloadKeyboardLayout': {'code': 0x14B1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hKl', 'type':'HKL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUnlockWindowStation': {'code': 0x14B2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWindowStation', 'type':'HWINSTA', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUnregisterHotKey': {'code': 0x14B3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hWnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'id', 'type':'INT', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUnregisterSessionPort': {'code': 0x14B4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	'NtUserUnregisterUserApiHook': {'code': 0x14B5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserUpdateDefaultDesktopThumbnail': {'code': 0x14B6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUpdateInputContext': {'code': 0x14B7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUpdateInstance': {'code': 0x14B8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown1', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwUnknown2', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUpdateLayeredWindow': {'code': 0x14B9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hwnd', 'type':'HWND', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdcDst', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptDst', 'type':'PPOINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'psize', 'type':'PSIZE', 'in': True, 'out': False, 'optional': False},
			{'name': 'hdcSrc', 'type':'HDC', 'in': True, 'out': False, 'optional': False},
			{'name': 'pptSrc', 'type':'PPOINT', 'in': True, 'out': False, 'optional': False},
			{'name': 'crKey', 'type':'COLORREF', 'in': True, 'out': False, 'optional': False},
			{'name': 'pblend', 'type':'PBLENDFUNCTION', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwFlags', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'prcDirty', 'type':'PRECT', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserUpdatePerUserSystemParameters': {'code': 0x14BA, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserUpdateWindowInputSinkHints': {'code': 0x14BB, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtUserUpdateWindowTrackingInfo': {'code': 0x14BC, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserUserHandleGrantAccess': {'code': 0x14BD, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hUserHandle', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'hJob', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'bGrant', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserValidateHandleSecure': {'code': 0x14BE, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hHdl', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown function until now
	'NtUserWOWCleanup': {'code': 0x14BF, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown parameter types
	'NtUserWaitAvailableMessageEx': {'code': 0x14C0, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserWaitForInputIdle': {'code': 0x14C1, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'hProcess', 'type':'HANDLE', 'in': True, 'out': False, 'optional': False},
			{'name': 'dwMilliseconds', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
			{'name': 'Unknown2', 'type':'BOOL', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserWaitForMsgAndEvent': {'code': 0x14C2, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'dwUnknown0', 'type':'DWORD', 'in': True, 'out': False, 'optional': False},
		]},

	'NtUserWaitForRedirectionStartComplete': {'code': 0x14C3, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserWindowFromDC': {'code': 0x14C4, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	'NtUserWindowFromPhysicalPoint': {'code': 0x14C5, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 1 ,'params':
		[
			{'name': 'x', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
			{'name': 'y', 'type':'LONG', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtValidateCompositionSurfaceHandle': {'code': 0x14C6, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
		[
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
			{'name': 'None', 'type':'?', 'in': True, 'out': False, 'optional': False},
		]},

	#TODO: Unknown parameter types
	'NtVisualCaptureBits': {'code': 0x14C7, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 2 ,'params':
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
	'NtUserSetClassLongPtr': {'code': 0x14C8, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

	#TODO: Unknown function until now
	'NtUserSetWindowLongPtr': {'code': 0x14C9, 'retVal':'NTSTATUS', 'lib': 'win32u.dll', 'level': 3 ,'params':
		[
		]},

}
