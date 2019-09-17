Data = \
{
	'POINT':
		[
			{'name': 'x', 'type': 'LONG'},
			{'name': 'y', 'type': 'LONG'}
		]
	, 'PPOINT': 'POINT*', 'LPPOINT': 'POINT*',

	'POINTL':
		[
			{'name': 'x', 'type': 'LONG'},
			{'name': 'y', 'type': 'LONG'}
		]
	, 'PPOINTL': 'POINTL*',

	'RGBQUAD':
		[
			{'name': 'rgbBlue', 'type': 'BYTE'},
			{'name': 'rgbGreen', 'type': 'BYTE'},
			{'name': 'rgbRed', 'type': 'BYTE'},
			{'name': 'rgbReserved', 'type': 'BYTE'}
		]
	, 'LPRGBQUAD': 'RGBQUAD*',

	'BITMAPINFOHEADER':
		[
			{'name': 'biSize', 'type': 'DWORD'},
			{'name': 'biWidth', 'type': 'LONG'},
			{'name': 'biHeight', 'type': 'LONG'},
			{'name': 'biPlanes', 'type': 'WORD'},
			{'name': 'biBitCount', 'type': 'WORD'},
			{'name': 'biCompression', 'type': 'DWORD'},
			{'name': 'biSizeImage', 'type': 'DWORD'},
			{'name': 'biXPelsPerMeter', 'type': 'LONG'},
			{'name': 'biYPelsPerMeter', 'type': 'LONG'},
			{'name': 'biClrUsed', 'type': 'DWORD'},
			{'name': 'biClrImportant', 'type': 'DWORD'},
		]
	, 'LPBITMAPINFOHEADER': 'BITMAPINFOHEADER*',

	'BITMAPINFO':
		[
			{'name': 'bmiHeader', 'type': 'BITMAPINFOHEADER'},
			{'name': 'bmiColors', 'type': 'RGBQUAD', 'array': 100} #TODO: Actually it's size is dependent of header.....
		]
	, 'LPBITMAPINFO': 'BITMAPINFO*',

	'DOCINFOW':
		[
			{'name': 'cbSize', 'type': 'INT'},
			{'name': 'lpszDocName', 'type': 'LPCWSTR'},
			{'name': 'lpszOutput', 'type': 'LPCWSTR'},
			{'name': 'lpszDatatype', 'type': 'LPCWSTR'},
			{'name': 'fwType', 'type': 'DWORD'}
		]
	, 'LPDOCINFOW': 'DOCINFOW*',

	'UNIVERSAL_FONT_ID':
		[
			{'name': 'CheckSum', 'type': 'ULONG'},
			{'name': 'Index', 'type': 'ULONG'}
		]
	, 'PUNIVERSAL_FONT_ID': 'UNIVERSAL_FONT_ID*',

	'COLORADJUSTMENT':
		[
			{'name': 'caSize', 'type': 'WORD'},
			{'name': 'caFlags', 'type': 'WORD'},
			{'name': 'caIlluminantIndex', 'type': 'WORD'},
			{'name': 'caRedGamma', 'type': 'WORD'},
			{'name': 'caGreenGamma', 'type': 'WORD'},
			{'name': 'caBlueGamma', 'type': 'WORD'},
			{'name': 'caReferenceBlack', 'type': 'WORD'},
			{'name': 'caReferenceWhite', 'type': 'WORD'},
			{'name': 'caContrast', 'type': 'SHORT'},
			{'name': 'caBrightness', 'type': 'SHORT'},
			{'name': 'caColorfulness', 'type': 'SHORT'},
			{'name': 'caRedGreenTint', 'type': 'SHORT'}
		]
	, 'PCOLORADJUSTMENT': 'COLORADJUSTMENT*',

	'RECT':
		[
			{'name': 'left', 'type': 'LONG'},
			{'name': 'top', 'type': 'LONG'},
			{'name': 'right', 'type': 'LONG'},
			{'name': 'bottom', 'type': 'LONG'}
		]
	, 'PRECT': 'RECT*', 'LPRECT': 'RECT*', 'LPCRECT': 'RECT*', 'PRECTFX': 'RECT*',


	 'RECTL':
		[
			{'name': 'left', 'type': 'LONG'},
			{'name': 'top', 'type': 'LONG'},
			{'name': 'right', 'type': 'LONG'},
			{'name': 'bottom', 'type': 'LONG'}
		]
	, 'PRECTL': 'RECTL*',

	'DEVMODEW':
		[
			{'name': 'dmDeviceName', 'type': 'WCHAR', 'arrya': 32},
			{'name': 'dmSpecVersion', 'type': 'WORD'},
			{'name': 'dmDriverVersion', 'type': 'WORD'},
			{'name': 'dmSize', 'type': 'WORD'},
			{'name': 'dmDriverExtra', 'type': 'WORD'},
			{'name': 'dmFields', 'type': 'DWORD'},
			{'name': 'dmOrientation', 'type': 'short'},
			{'name': 'dmPaperSize', 'type': 'short'},
			{'name': 'dmPaperLength', 'type': 'short'},
			{'name': 'dmPaperWidth', 'type': 'short'},
			{'name': 'dmScale', 'type': 'short'},
			{'name': 'dmCopies', 'type': 'short'},
			{'name': 'dmDefaultSource', 'type': 'short'},
			{'name': 'dmPrintQuality', 'type': 'short'},
			{'name': 'dmColor', 'type': 'short'},
			{'name': 'dmDuplex', 'type': 'short'},
			{'name': 'dmYResolution', 'type': 'short'},
			{'name': 'dmTTOption', 'type': 'short'},
			{'name': 'dmCollate', 'type': 'short'},
			{'name': 'dmFormName', 'type': 'WCHAR', 'array': 32},
			{'name': 'dmLogPixels', 'type': 'WORD'},
			{'name': 'dmBitsPerPel', 'type': 'DWORD'},
			{'name': 'dmPelsWidth', 'type': 'DWORD'},
			{'name': 'dmPelsHeight', 'type': 'DWORD'},
			{'name': 'dmDisplayFlags', 'type': 'DWORD'},
			{'name': 'dmDisplayFrequency', 'type': 'DWORD'},
			{'name': 'dmICMMethod', 'type': 'DWORD'},
			{'name': 'dmICMIntent', 'type': 'DWORD'},
			{'name': 'dmMediaType', 'type': 'DWORD'},
			{'name': 'dmDitherType', 'type': 'DWORD'},
			{'name': 'dmReserved1', 'type': 'DWORD'},
			{'name': 'dmReserved2', 'type': 'DWORD'},
			{'name': 'dmPanningWidth', 'type': 'DWORD'},
			{'name': 'dmPanningHeight', 'type': 'DWORD'},
		]
	, 'LPDEVMODEW': 'DEVMODEW*',

	'DRIVER_INFO_2W':
		[
			{'name': 'cVersion', 'type': 'DWORD'},
			{'name': 'pName', 'type': 'LPWSTR'},
			{'name': 'pEnvironment', 'type': 'LPWSTR'},
			{'name': 'pDriverPath', 'type': 'LPWSTR'},
			{'name': 'pDataFile', 'type': 'LPWSTR'},
			{'name': 'pConfigFile', 'type': 'LPWSTR'},
		]
	, 'PDRIVER_INFO_2W': 'DRIVER_INFO_2W*',

	'DESIGNVECTOR':
		[
			{'name': 'dvReserved', 'type': 'DWORD'},
			{'name': 'dvNumAxes', 'type': 'DWORD'},
			{'name': 'dvValues', 'type': 'LONG', 'array': 16},
		]
	, 'PDESIGNVECTOR': 'DESIGNVECTOR*',

	'POLYTEXTW':
		[
			{'name': 'x', 'type': 'int'},
			{'name': 'y', 'type': 'int'},
			{'name': 'n', 'type': 'UINT'},
			{'name': 'lpstr', 'type': 'LPCTSTR'},
			{'name': 'uiFlags', 'type': 'UINT'},
			{'name': 'rcl', 'type': 'RECT'},
			{'name': 'pdx', 'type': 'PINT'}
		]
	, 'PPOLYTEXTW': 'POLYTEXTW*',

	'PALETTEENTRY':
		[
			{'name': 'rgbBlue', 'type': 'BYTE'},
			{'name': 'rgbGreen', 'type': 'BYTE'},
			{'name': 'rgbRed', 'type': 'BYTE'},
			{'name': 'rgbReserved', 'type': 'BYTE'}
		]
	, 'PPALETTEENTRY': 'PALETTEENTRY*', 'LPPALETTEENTRY': 'PALETTEENTRY*',

	'LOGPALETTE':
		[
			{'name': 'palVersion', 'type': 'WORD', 'values': [0x300]},
			{'name': 'palNumEntries', 'type': 'WORD'},
			{'name': 'palPalEntry', 'type': 'PALETTEENTRY', 'array': 10}
		]
	, 'PLOGPALETTE': 'LOGPALETTE*',

	'POLYPATBLT':
		[
			{'name': 'nXLeft', 'type': 'INT'},
			{'name': 'nYLeft', 'type': 'INT'},
			{'name': 'nWidth', 'type': 'INT'},
			{'name': 'nHeight', 'type': 'INT'},
			{'name': 'hBrush', 'type': 'HBRUSH'}
		]
	, 'PPOLYPATBLT': 'POLYPATBLT*',

	'XFORM':
		[
			{'name': 'eM11', 'type': 'FLOAT'},
			{'name': 'eM12', 'type': 'FLOAT'},
			{'name': 'eM21', 'type': 'FLOAT'},
			{'name': 'eM22', 'type': 'FLOAT'},
			{'name': 'eDx', 'type': 'FLOAT'},
			{'name': 'eDy', 'type': 'FLOAT'},
		]
	, 'LPXFORM': 'XFORM*',

	'LOGFONT':
		[
			{'name': 'lfHeight', 'type': 'LONG'},
			{'name': 'lfWidth', 'type': 'LONG'},
			{'name': 'lfEscapement', 'type': 'LONG'},
			{'name': 'lfOrientation', 'type': 'LONG'},
			{'name': 'lfWeight', 'type': 'LONG'},
			{'name': 'lfItalic', 'type': 'BYTE'},
			{'name': 'lfUnderline', 'type': 'BYTE'},
			{'name': 'lfStrikeOut', 'type': 'BYTE'},
			{'name': 'lfCharSet', 'type': 'BYTE'},
			{'name': 'lfOutPrecision', 'type': 'BYTE'},
			{'name': 'lfClipPrecision', 'type': 'BYTE'},
			{'name': 'lfQuality', 'type': 'BYTE'},
			{'name': 'lfPitchAndFamily', 'type': 'BYTE'},
			{'name': 'lfFaceName', 'type': 'TCHAR', 'array': 32},
		]
	, 'PLOGFONT': 'LOGFONT*',

	'ENUMLOGFONTEX':
		[
			{'name': 'eM11', 'type': 'LOGFONT'},
			{'name': 'eM12', 'type': 'TCHAR', 'array': 64},
			{'name': 'eM21', 'type': 'TCHAR', 'array': 32},
			{'name': 'eM22', 'type': 'TCHAR', 'array': 32}
		]
	, 'LPENUMLOGFONTEX': 'ENUMLOGFONTEX*',

	'DESIGNVECTOR':
		[
			{'name': 'dvReserved', 'type': 'DWORD'},
			{'name': 'dvNumAxes', 'type': 'DWORD'},
			{'name': 'dvValues', 'type': 'LONG', 'array': 16}
		]
	, 'PDESIGNVECTOR': 'DESIGNVECTOR*',

	'ENUMLOGFONTEXDVW':
		[
			{'name': 'elfEnumLogfontEx', 'type': 'ENUMLOGFONTEX'},
			{'name': 'elfDesignVector', 'type': 'DESIGNVECTOR'},
		]
	, 'PENUMLOGFONTEXDVW': 'ENUMLOGFONTEXDVW*',

	'TRIVERTEX':
		[
			{'name': 'x', 'type': 'LONG'},
			{'name': 'y', 'type': 'LONG'},
			{'name': 'Red', 'type': 'COLOR16'},
			{'name': 'Green', 'type': 'COLOR16'},
			{'name': 'Blue', 'type': 'COLOR16'},
			{'name': 'Alpha', 'type': 'COLOR16'},
		]
	, 'PTRIVERTEX': 'TRIVERTEX*',

	'WIDTHDATA':
		[
			{'name': 'sOverhang', 'type': 'USHORT'},
			{'name': 'sHeight', 'type': 'USHORT'},
			{'name': 'sCharInc', 'type': 'USHORT'},
			{'name': 'sBreak', 'type': 'USHORT'},
			{'name': 'jFirst', 'type': 'BYTE'},
			{'name': 'jLast', 'type': 'BYTE'},
			{'name': 'jBreak', 'type': 'BYTE'},
			{'name': 'jDefault', 'type': 'BYTE'},
			{'name': 'sDBCSInc', 'type': 'USHORT'},
			{'name': 'sDefaultInc', 'type': 'USHORT'},
		]
	, 'PWIDTHDATA': 'WIDTHDATA*',

	'WCRANGE':
		[
			{'name': 'wcLow', 'type': 'WCHAR'},
			{'name': 'cGlyphs', 'type': 'USHORT'},
		]
	, 'PWCRANGE': 'WCRANGE*',

	'GLYPHSET':
		[
			{'name': 'cbThis', 'type': 'DWORD'},
			{'name': 'flAccel', 'type': 'DWORD'},
			{'name': 'cGlyphsSupported', 'type': 'DWORD'},
			{'name': 'cRanges', 'type': 'DWORD'},
			{'name': 'ranges', 'type': 'WCRANGE'},
		]
	, 'LPGLYPHSET': 'GLYPHSET*',
	
	'TEXTMETRICW':
		[
			{'name': 'tmHeight', 'type': 'LONG'},
			{'name': 'tmAscent', 'type': 'LONG'},
			{'name': 'tmDescent', 'type': 'LONG'},
			{'name': 'tmInternalLeading', 'type': 'LONG'},
			{'name': 'tmExternalLeading', 'type': 'LONG'},
			{'name': 'tmAveCharWidth', 'type': 'LONG'},
			{'name': 'tmMaxCharWidth', 'type': 'LONG'},
			{'name': 'tmWeight', 'type': 'LONG'},
			{'name': 'tmOverhang', 'type': 'LONG'},
			{'name': 'tmDigitizedAspectX', 'type': 'LONG'},
			{'name': 'tmDigitizedAspectY', 'type': 'LONG'},
			{'name': 'tmFirstChar', 'type': 'TCHAR'},
			{'name': 'tmLastChar', 'type': 'TCHAR'},
			{'name': 'tmDefaultChar', 'type': 'TCHAR'},
			{'name': 'tmBreakChar', 'type': 'TCHAR'},
			{'name': 'tmItalic', 'type': 'BYTE'},
			{'name': 'tmUnderlined', 'type': 'BYTE'},
			{'name': 'tmStruckOut', 'type': 'BYTE'},
			{'name': 'tmPitchAndFamily', 'type': 'BYTE'},
			{'name': 'tmCharSet', 'type': 'BYTE'},
		]
	, 'PTEXTMETRICW': 'TEXTMETRICW*',

	'TMDIFF':
		[
			{'name': 'cjotma', 'type': 'ULONG'},
			{'name': 'chFirst', 'type': 'CHAR'},
			{'name': 'chLast', 'type': 'CHAR'},
			{'name': 'ChDefault', 'type': 'CHAR'},
			{'name': 'ChBreak', 'type': 'CHAR'},
		]
	, 'PTMDIFF': 'TMDIFF*',

	'TMW_INTERNAL':
		[
			{'name': 'TextMetric', 'type': 'TEXTMETRICW'},
			{'name': 'Diff', 'type': 'TMDIFF'},
		]
	, 'PTMW_INTERNAL': 'TMW_INTERNAL*',

	'FONTSIGNATURE':
		[
			{'name': 'fsUsb', 'type': 'DWORD', 'array': 4},
			{'name': 'fsCsb', 'type': 'DWORD', 'array': 2},
		]
	, 'LPFONTSIGNATURE': 'FONTSIGNATURE*',

	'RASTERIZER_STATUS':
		[
			{'name': 'nSize', 'type': 'short'},
			{'name': 'wFlags', 'type': 'short'},
			{'name': 'nLanguageID', 'type': 'short'},
		]
	, 'LPRASTERIZER_STATUS': 'RASTERIZER_STATUS*',

	'KERNINGPAIR':
		[
			{'name': 'wFirst', 'type': 'WORD'},
			{'name': 'wSecond', 'type': 'WORD'},
			{'name': 'iKernAmount', 'type': 'int'},
		]
	, 'PKERNINGPAIR': 'KERNINGPAIR*',

	'PANOSE':
		[
			{'name': 'bFamilyType', 'type': 'BYTE'},
			{'name': 'bSerifStyle', 'type': 'BYTE'},
			{'name': 'bWeight', 'type': 'BYTE'},
			{'name': 'bProportion', 'type': 'BYTE'},
			{'name': 'bContrast', 'type': 'BYTE'},
			{'name': 'bStrokeVariation', 'type': 'BYTE'},
			{'name': 'bArmStyle', 'type': 'BYTE'},
			{'name': 'bLetterform', 'type': 'BYTE'},
			{'name': 'bMidline', 'type': 'BYTE'},
			{'name': 'bXHeight', 'type': 'BYTE'},
		]
	, 'LPPANOSE': 'PANOSE*',

	'OUTLINETEXTMETRICW':
		[
			{'name': 'otmSize', 'type': 'UINT'},
			{'name': 'otmTextMetrics', 'type': 'TEXTMETRICW'},
			{'name': 'otmFiller', 'type': 'BYTE'},
			{'name': 'otmPanoseNumber', 'type': 'PANOSE'},
			{'name': 'otmfsSelection', 'type': 'INT'},
			{'name': 'otmfsType', 'type': 'INT'},
			{'name': 'otmsCharSlopeRise', 'type': 'INT'},
			{'name': 'otmsCharSlopeRun', 'type': 'INT'},
			{'name': 'otmItalicAngle', 'type': 'INT'},
			{'name': 'otmEMSquare', 'type': 'INT'},
			{'name': 'otmAscent', 'type': 'INT'},
			{'name': 'otmDescent', 'type': 'INT'},
			{'name': 'otmLineGap', 'type': 'INT'},
			{'name': 'otmsCapEmHeight', 'type': 'INT'},
			{'name': 'otmsXHeight', 'type': 'INT'},
			{'name': 'otmrcFontBox', 'type': 'RECT'},
			{'name': 'otmMacAscent', 'type': 'INT'},
			{'name': 'otmMacDescent', 'type': 'INT'},
			{'name': 'otmMacLineGap', 'type': 'INT'},
			{'name': 'otmusMinimumPPEM', 'type': 'INT'},
			{'name': 'otmptSubscriptSize', 'type': 'POINT'},
			{'name': 'otmptSubscriptOffset', 'type': 'POINT'},
			{'name': 'otmptSuperscriptSize', 'type': 'POINT'},
			{'name': 'otmptSuperscriptOffset', 'type': 'POINT'},
			{'name': 'otmsStrikeoutSize', 'type': 'INT'},
			{'name': 'otmsStrikeoutPosition', 'type': 'INT'},
			{'name': 'otmsUnderscoreSize', 'type': 'INT'},
			{'name': 'otmsUnderscorePosition', 'type': 'INT'},
			{'name': 'otmpFamilyName', 'type': 'PSTR'},
			{'name': 'otmpFaceName', 'type': 'PSTR'},
			{'name': 'otmpStyleName', 'type': 'PSTR'},
			{'name': 'otmpFullName', 'type': 'PSTR'},
		]
	, 'POUTLINETEXTMETRICW': 'OUTLINETEXTMETRICW*',

	'GLYPHMETRICS':
		[
			{'name': 'gmBlackBoxX', 'type': 'UINT'},
			{'name': 'gmBlackBoxY', 'type': 'UINT'},
			{'name': 'gmptGlyphOrigin', 'type': 'POINT'},
			{'name': 'gmCellIncX', 'type': 'SHORT'},
			{'name': 'gmCellIncY', 'type': 'SHORT'},
		]
	, 'LPGLYPHMETRICS': 'GLYPHMETRICS*',

	'FIXED':
		[
			{'name': 'fract', 'type': 'WORD'},
			{'name': 'value', 'type': 'short'},
		]
	, 'PFIXED': 'FIXED*',

	'MAT2':
		[
			{'name': 'eM11', 'type': 'FIXED'},
			{'name': 'eM12', 'type': 'FIXED'},
			{'name': 'eM21', 'type': 'FIXED'},
			{'name': 'eM22', 'type': 'FIXED'},
		]
	, 'LPMAT2': 'MAT2*',

	'EXTTEXTMETRIC':
		[
			{'name': 'emSize', 'type': 'SHORT'},
			{'name': 'emPointSize', 'type': 'SHORT'},
			{'name': 'emOrientation', 'type': 'SHORT'},
			{'name': 'emMasterHeight', 'type': 'SHORT'},
			{'name': 'emMinScale', 'type': 'SHORT'},
			{'name': 'emMaxScale', 'type': 'SHORT'},
			{'name': 'emMasterUnits', 'type': 'SHORT'},
			{'name': 'emCapHeight', 'type': 'SHORT'},
			{'name': 'emXHeight', 'type': 'SHORT'},
			{'name': 'emLowerCaseAscent', 'type': 'SHORT'},
			{'name': 'emLowerCaseDescent', 'type': 'SHORT'},
			{'name': 'emSlant', 'type': 'SHORT'},
			{'name': 'emSuperScript', 'type': 'SHORT'},
			{'name': 'emSubScript', 'type': 'SHORT'},
			{'name': 'emSuperScriptSize', 'type': 'SHORT'},
			{'name': 'emSubScriptSize', 'type': 'SHORT'},
			{'name': 'emUnderlineOffset', 'type': 'SHORT'},
			{'name': 'emUnderlineWidth', 'type': 'SHORT'},
			{'name': 'emDoubleUpperUnderlineOffset', 'type': 'SHORT'},
			{'name': 'emDoubleLowerUnderlineOffset', 'type': 'SHORT'},
			{'name': 'emDoubleUpperUnderlineWidth', 'type': 'SHORT'},
			{'name': 'emDoubleLowerUnderlineWidth', 'type': 'SHORT'},
			{'name': 'emStrikeOutOffset', 'type': 'SHORT'},
			{'name': 'emStrikeOutWidth', 'type': 'SHORT'},
			{'name': 'emKernPairs', 'type': 'WORD'},
			{'name': 'emKernTracks', 'type': 'WORD'},
		]
	, 'PEXTTEXTMETRIC': 'EXTTEXTMETRIC*',

	'DEVCAPS':
		[
			{'name': 'ulVersion', 'type': 'ULONG'},
			{'name': 'ulTechnology', 'type': 'ULONG'},
			{'name': 'ulHorzSizeM', 'type': 'ULONG'},
			{'name': 'ulVertSizeM', 'type': 'ULONG'},
			{'name': 'ulHorzSize', 'type': 'ULONG'},
			{'name': 'ulVertSize', 'type': 'ULONG'},
			{'name': 'ulHorzRes', 'type': 'ULONG'},
			{'name': 'ulVertRes', 'type': 'ULONG'},
			{'name': 'ulBitsPixel', 'type': 'ULONG'},
			{'name': 'ulPlanes', 'type': 'ULONG'},
			{'name': 'ulNumPens', 'type': 'ULONG'},
			{'name': 'ulNumFonts', 'type': 'ULONG'},
			{'name': 'ulNumColors', 'type': 'ULONG'},
			{'name': 'ulRasterCaps', 'type': 'ULONG'},
			{'name': 'ulAspectX', 'type': 'ULONG'},
			{'name': 'ulAspectY', 'type': 'ULONG'},
			{'name': 'ulAspectXY', 'type': 'ULONG'},
			{'name': 'ulLogPixelsX', 'type': 'ULONG'},
			{'name': 'ulLogPixelsY', 'type': 'ULONG'},
			{'name': 'ulSizePalette', 'type': 'ULONG'},
			{'name': 'ulColorRes', 'type': 'ULONG'},
			{'name': 'ulPhysicalWidth', 'type': 'ULONG'},
			{'name': 'ulPhysicalHeight', 'type': 'ULONG'},
			{'name': 'ulPhysicalOffsetX', 'type': 'ULONG'},
			{'name': 'ulPhysicalOffsetY', 'type': 'ULONG'},
			{'name': 'ulTextCaps', 'type': 'ULONG'},
			{'name': 'ulVRefresh', 'type': 'ULONG'},
			{'name': 'ulDesktopHorzRes', 'type': 'ULONG'},
			{'name': 'ulDesktopVertRes', 'type': 'ULONG'},
			{'name': 'ulBltAlignment', 'type': 'ULONG'},
			{'name': 'ulPanningHorzRes', 'type': 'ULONG'},
			{'name': 'ulPanningVertRes', 'type': 'ULONG'},
			{'name': 'xPanningAlignment', 'type': 'ULONG'},
			{'name': 'yPanningAlignment', 'type': 'ULONG'},
			{'name': 'ulShadeBlend', 'type': 'ULONG'},
			{'name': 'ulColorMgmtCaps', 'type': 'ULONG'},
		]
	, 'PDEVCAPS': 'DEVCAPS*',

	'GCP_RESULTSW':
		[
			{'name': 'lStructSize', 'type': 'DWORD'},
			{'name': 'lpOutString', 'type': 'LPWSTR'},
			{'name': 'lpOrder', 'type': 'PUINT'},
			{'name': 'lpDx', 'type': 'PINT'},
			{'name': 'lpCaretPos', 'type': 'PINT'},
			{'name': 'lpClass', 'type': 'LPWSTR'},
			{'name': 'lpGlyphs', 'type': 'LPWSTR'},
			{'name': 'nGlyphs', 'type': 'UINT'},
			{'name': 'nMaxFit', 'type': 'UINT'},
		]
	, 'LPGCP_RESULTSW': 'GCP_RESULTSW*',

	'CHWIDTHINFO':
		[
			{'name': 'lMinA', 'type': 'LONG'},
			{'name': 'lMinC', 'type': 'LONG'},
			{'name': 'lMinD', 'type': 'LONG'},
		]
	, 'PCHWIDTHINFO': 'CHWIDTHINFO*',

	'RGNDATAHEADER':
		[
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'iType', 'type': 'DWORD'},
			{'name': 'nCount', 'type': 'DWORD'},
			{'name': 'nRgnSize', 'type': 'DWORD'},
			{'name': 'rcBound', 'type': 'RECT'},
		]
	, 'PRGNDATAHEADER': 'RGNDATAHEADER*',

	'RGNDATA':
		[
			{'name': 'rdh', 'type': 'RGNDATAHEADER'},
			{'name': 'buffer', 'type': 'CHAR', 'array': 100} #TODO: Actually it's size is dependent of header.....
		]
	, 'LPRGNDATA': 'RGNDATA*',

	'SIZE':
		[
			{'name': 'cx', 'type': 'LONG'},
			{'name': 'cy', 'type': 'LONG'},
		]
	, 'PSIZE': 'SIZE*',

	'PERBANDINFO':
		[
			{'name': 'bRepeatThisBand', 'type': 'BOOL'},
			{'name': 'szlBand', 'type': 'SIZE'},
			{'name': 'ulHorzRes', 'type': 'ULONG'},
			{'name': 'ulVertRes', 'type': 'ULONG'},
		]
	, 'PPERBANDINFO': 'PERBANDINFO*',

	'DDVIDEOPORTCONNECT':
		[
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'dwPortWidth', 'type': 'DWORD'},
			{'name': 'guidTypeID', 'type': 'GUID'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'dwReserved1', 'type': 'ULONG_PTR'},
		]
	, 'LPDDVIDEOPORTCONNECT': 'DDVIDEOPORTCONNECT*',

	'DDVIDEOPORTNOTIFY':
		[
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'bInUse', 'type': 'BOOL'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'dwReserved1', 'type': 'DWORD'},
			{'name': 'VideoPortType', 'type': 'DDVIDEOPORTCONNECT'},
			{'name': 'dwReserved2', 'type': 'ULONG_PTR'},
			{'name': 'dwReserved3', 'type': 'ULONG_PTR'},
		]
	, 'LPDDVIDEOPORTNOTIFY': 'DDVIDEOPORTNOTIFY*',

	'DDVIDEOPORTCAPS':
		[
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'bInUse', 'type': 'BOOL'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'dwReserved1', 'type': 'DWORD'},
			{'name': 'VideoPortType', 'type': 'DDVIDEOPORTCONNECT'},
			{'name': 'dwReserved2', 'type': 'ULONG_PTR'},
			{'name': 'dwReserved3', 'type': 'ULONG_PTR'},
		]
	, 'LPDDVIDEOPORTCAPS': 'DDVIDEOPORTCAPS*',

	'DD_DIRECTDRAW_GLOBAL':
		[
			{'name': 'dhpdev', 'type': 'PVOID'},
			{'name': 'dwReserved1', 'type': 'ULONG_PTR'},
			{'name': 'dwReserved2', 'type': 'ULONG_PTR'},
			{'name': 'lpDDVideoPortCaps', 'type': 'LPDDVIDEOPORTCAPS'},
		]
	, 'PDD_DIRECTDRAW_GLOBAL': 'DD_DIRECTDRAW_GLOBAL*',

	'DD_DIRECTDRAW_LOCAL':
		[
			{'name': 'lpGbl', 'type': 'PDD_DIRECTDRAW_GLOBAL'},
		]
	, 'PDD_DIRECTDRAW_LOCAL': 'DD_DIRECTDRAW_LOCAL*',

	'DDVIDEOPORTDESC':
		[
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'dwFieldWidth', 'type': 'DWORD'},
			{'name': 'dwVBIWidth', 'type': 'DWORD'},
			{'name': 'dwFieldHeight', 'type': 'DWORD'},
			{'name': 'dwMicrosecondsPerField', 'type': 'DWORD'},
			{'name': 'dwMaxPixelsPerSecond', 'type': 'DWORD'},
			{'name': 'dwVideoPortID', 'type': 'DWORD'},
			{'name': 'dwReserved1', 'type': 'DWORD'},
			{'name': 'VideoPortType', 'type': 'DDVIDEOPORTCONNECT'},
			{'name': 'dwReserved2', 'type': 'ULONG_PTR'},
			{'name': 'dwReserved3', 'type': 'ULONG_PTR'},
		]
	, 'LPDDVIDEOPORTDESC': 'DDVIDEOPORTDESC*',

	'DDPIXELFORMAT':
		[
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'dwFourCC', 'type': 'DWORD'},
			{'name': 'dwRGBBitCount', 'type': 'DWORD'},
			{'name': 'dwRBitMask', 'type': 'DWORD'},
			{'name': 'dwGBitMask', 'type': 'DWORD'},
			{'name': 'dwBBitMask', 'type': 'DWORD'},
			{'name': 'dwRGBAlphaBitMask', 'type': 'DWORD'},
		]
	, 'LPDDPIXELFORMAT': 'DDPIXELFORMAT*',

	'DDVIDEOPORTINFO':
		[
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'dwOriginX', 'type': 'DWORD'},
			{'name': 'dwOriginY', 'type': 'DWORD'},
			{'name': 'dwVPFlags', 'type': 'DWORD'},
			{'name': 'rCrop', 'type': 'RECT'},
			{'name': 'dwPrescaleWidth', 'type': 'DWORD'},
			{'name': 'dwPrescaleHeight', 'type': 'DWORD'},
			{'name': 'lpddpfInputFormat', 'type': 'LPDDPIXELFORMAT'},
			{'name': 'lpddpfVBIInputFormat', 'type': 'LPDDPIXELFORMAT'},
			{'name': 'lpddpfVBIOutputFormat', 'type': 'LPDDPIXELFORMAT'},
			{'name': 'dwVBIHeight', 'type': 'DWORD'},
			{'name': 'dwReserved1', 'type': 'ULONG_PTR'},
			{'name': 'dwReserved2', 'type': 'ULONG_PTR'},
		]
	, 'LPDDVIDEOPORTINFO': 'DDVIDEOPORTINFO*',

	'VIDEOMEMORY':
		[
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'fpStart', 'type': 'FLATPTR'},
			{'name': 'fpEnd', 'type': 'FLATPTR'},
			{'name': 'ddsCaps', 'type': 'DDSCAPS'},
			{'name': 'ddsCapsAlt', 'type': 'DDSCAPS'},
			{'name': 'dwHeight', 'type': 'DWORD'},  #TODO: Is union with VMEMHEAP*
		]
	, 'PVIDEOMEMORY': 'VIDEOMEMORY*',

	'DD_SURFACE_GLOBAL':
		[
			{'name': 'dwBlockSizeY', 'type': 'DWORD'},
			{'name': 'lpVidMemHeap', 'type': 'PVIDEOMEMORY'},
			{'name': 'fpVidMem', 'type': 'FLATPTR'},
			{'name': 'lPitch', 'type': 'LONG'},
			{'name': 'yHint', 'type': 'LONG'},
			{'name': 'xHint', 'type': 'LONG'},
			{'name': 'wHeight', 'type': 'DWORD'},
			{'name': 'wWidth', 'type': 'DWORD'},
			{'name': 'dwReserved1', 'type': 'ULONG_PTR'},
			{'name': 'ddpfSurface', 'type': 'DDPIXELFORMAT'},
			{'name': 'fpHeapOffset', 'type': 'FLATPTR'},
			{'name': 'hCreatorProcess', 'type': 'HANDLE'},
		]
	, 'PDD_SURFACE_GLOBAL': 'DD_SURFACE_GLOBAL*',

	'DDSCAPS':
		[
			{'name': 'dwCaps', 'type': 'DWORD'},
		]
	, 'LPDDSCAPS': 'DDSCAPS*',

	'DDCOLORKEY':
		[
			{'name': 'dw1', 'type': 'DWORD'},
			{'name': 'dw2', 'type': 'DWORD'},
		]
	, 'LPDDCOLORKEY': 'DDCOLORKEY*',

	'DDSCAPSEX':
		[
			{'name': 'dwCaps2', 'type': 'DWORD'},
			{'name': 'dwCaps3', 'type': 'DWORD'},
		]
	, 'LPDDSCAPSEX': 'DDSCAPSEX*',

	'DD_SURFACE_MORE':
		[
			{'name': 'dwMipMapCount', 'type': 'DWORD'},
			{'name': 'lpVideoPort', 'type': 'PVOID'}, #TODO: Should be PDD_VIDEOPORT_LOCAL but that would create circle in structures.....
			{'name': 'dwOverlayFlags', 'type': 'DWORD'},
			{'name': 'ddsCapsEx', 'type': 'DDSCAPSEX'},
			{'name': 'dwSurfaceHandle', 'type': 'DWORD'},
		]
	, 'PDD_SURFACE_MORE': 'DD_SURFACE_MORE*',

	'DD_ATTACHLIST':
		[
			{'name': 'lpLink', 'type': 'PVOID'}, #TODO: Actually is with type PDD_ATTACHLIST, but self pointing dows not work
			{'name': 'lpAttached', 'type': 'PVOID'},#TODO: Actually is with type PDD_SURFACE_LOCAL, but create circle in structures.....
		]
	, 'PDD_ATTACHLIST': 'DD_ATTACHLIST*',


	'DD_SURFACE_LOCAL':
		[
			{'name': 'lpGbl', 'type': 'PDD_SURFACE_GLOBAL'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'ddsCaps', 'type': 'DDSCAPS'},
			{'name': 'dwReserved1', 'type': 'ULONG_PTR'},
			{'name': 'ddckCKSrcOverlay', 'type': 'DDCOLORKEY'},
			{'name': 'ddckCKDestOverlay', 'type': 'DDCOLORKEY'},
			{'name': 'lpSurfMore', 'type': 'PDD_SURFACE_MORE'},
			{'name': 'lpAttachList', 'type': 'PDD_ATTACHLIST'},
			{'name': 'lpAttachListFrom', 'type': 'PDD_ATTACHLIST'},
			{'name': 'rcOverlaySrc', 'type': 'RECT'},
		]
	, 'PDD_SURFACE_LOCAL': 'DD_SURFACE_LOCAL*',

	'DD_SURFACE_INT':
		[
			{'name': 'lpLcl', 'type': 'PDD_SURFACE_LOCAL'},
		]
	, 'PDD_SURFACE_INT': 'DD_SURFACE_INT*', 'PPDD_SURFACE_INT': 'PDD_SURFACE_INT*',

	'DD_VIDEOPORT_LOCAL':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'ddvpDesc', 'type': 'DDVIDEOPORTDESC'},
			{'name': 'ddvpInfo', 'type': 'DDVIDEOPORTINFO'},
			{'name': 'lpSurface', 'type': 'PDD_SURFACE_INT'},
			{'name': 'lpVBISurface', 'type': 'PDD_SURFACE_INT'},
			{'name': 'dwNumAutoflip', 'type': 'DWORD'},
			{'name': 'dwNumVBIAutoflip', 'type': 'DWORD'},
			{'name': 'dwReserved1', 'type': 'ULONG_PTR'},
			{'name': 'dwReserved2', 'type': 'ULONG_PTR'},
			{'name': 'dwReserved3', 'type': 'ULONG_PTR'},
		]
	, 'PDD_VIDEOPORT_LOCAL': 'DD_VIDEOPORT_LOCAL*',


	'DD_WAITFORVPORTSYNCDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'dwLine', 'type': 'DWORD'},
			{'name': 'dwTimeOut', 'type': 'DWORD'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'UpdateVideoPort', 'type': 'PVOID'},
		]
	, 'PDD_WAITFORVPORTSYNCDATA': 'DD_WAITFORVPORTSYNCDATA*',


	'DD_UPDATEVPORTDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'lplpDDSurface', 'type': 'PPDD_SURFACE_INT'},
			{'name': 'lplpDDVBISurface', 'type': 'PPDD_SURFACE_INT'},
			{'name': 'lpVideoInfo', 'type': 'LPDDVIDEOPORTINFO'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'dwNumAutoflip', 'type': 'DWORD'},
			{'name': 'dwNumVBIAutoflip', 'type': 'DWORD'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'UpdateVideoPort', 'type': 'PVOID'},
		]
	, 'PDD_UPDATEVPORTDATA': 'DD_UPDATEVPORTDATA*',

	'DD_GETVPORTSIGNALDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'dwStatus', 'type': 'DWORD'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'GetVideoSignalStatus', 'type': 'PVOID'},
		]
	, 'PDD_GETVPORTSIGNALDATA': 'DD_GETVPORTSIGNALDATA*',

	'DD_GETVPORTCONNECTDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'dwPortId', 'type': 'DWORD'},
			{'name': 'lpConnect', 'type': 'LPDDVIDEOPORTCONNECT'},
			{'name': 'dwNumEntries', 'type': 'DWORD'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'GetVideoPortConnectInfo', 'type': 'PVOID'},
		]
	, 'PDD_GETVPORTCONNECTDATA': 'DD_GETVPORTCONNECTDATA*',

	'DD_GETVPORTOUTPUTFORMATDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'lpddpfInputFormat', 'type': 'LPDDPIXELFORMAT'},
			{'name': 'lpddpfOutputFormats', 'type': 'LPDDPIXELFORMAT'},
			{'name': 'dwNumFormats', 'type': 'DWORD'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'GetVideoPortInputFormats', 'type': 'PVOID'},
		]
	, 'PDD_GETVPORTOUTPUTFORMATDATA': 'DD_GETVPORTOUTPUTFORMATDATA*',

	'DD_GETVPORTLINEDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'dwLine', 'type': 'DWORD'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'GetVideoPortLine', 'type': 'PVOID'},
		]
	, 'PDD_GETVPORTLINEDATA': 'DD_GETVPORTLINEDATA*',

	'DD_GETVPORTINPUTFORMATDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'lpddpfFormat', 'type': 'LPDDPIXELFORMAT'},
			{'name': 'dwNumFormats', 'type': 'DWORD'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'GetVideoPortInputFormats', 'type': 'PVOID'},
		]
	, 'PDD_GETVPORTINPUTFORMATDATA': 'DD_GETVPORTINPUTFORMATDATA*',

	'DD_GETVPORTFLIPSTATUSDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'fpSurface', 'type': 'FLATPTR'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'GetVideoPortFlipStatus', 'type': 'PVOID'},
		]
	, 'PDD_GETVPORTFLIPSTATUSDATA': 'DD_GETVPORTFLIPSTATUSDATA*',

	'DD_GETVPORTFIELDDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'bField', 'type': 'BOOL'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'GetVideoPortField', 'type': 'PVOID'},
		]
	, 'PDD_GETVPORTFIELDDATA': 'DD_GETVPORTFIELDDATA*',

	'DDVIDEOPORTBANDWIDTH':
		[
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'dwOverlay', 'type': 'DWORD'},
			{'name': 'dwColorkey', 'type': 'DWORD'},
			{'name': 'dwYInterpolate', 'type': 'DWORD'},
			{'name': 'dwYInterpAndColorkey', 'type': 'DWORD'},
			{'name': 'dwReserved1', 'type': 'ULONG_PTR'},
			{'name': 'dwReserved2', 'type': 'ULONG_PTR'},
		]
	, 'LPDDVIDEOPORTBANDWIDTH': 'DDVIDEOPORTBANDWIDTH*',

	'DD_GETVPORTBANDWIDTHDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'lpddpfFormat', 'type': 'LPDDPIXELFORMAT'},
			{'name': 'dwWidth', 'type': 'DWORD'},
			{'name': 'dwHeight', 'type': 'DWORD'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'lpBandwidth', 'type': 'LPDDVIDEOPORTBANDWIDTH'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'GetVideoPortBandwidth', 'type': 'PVOID'},
		]
	, 'PDD_GETVPORTBANDWIDTHDATA': 'DD_GETVPORTBANDWIDTHDATA*',

	'DD_FLIPVPORTDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'lpSurfCurr', 'type': 'PDD_SURFACE_LOCAL'},
			{'name': 'lpSurfTarg', 'type': 'PDD_SURFACE_LOCAL'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'FlipVideoPort', 'type': 'PVOID'},
		]
	, 'PDD_FLIPVPORTDATA': 'DD_FLIPVPORTDATA*',

	'DD_DESTROYVPORTDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'DestroyVideoPort', 'type': 'PVOID'},
		]
	, 'PDD_DESTROYVPORTDATA': 'DD_DESTROYVPORTDATA*',

	'DD_CREATEVPORTDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpDDVideoPortDesc', 'type': 'LPDDVIDEOPORTDESC'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'DestroyVideoPort', 'type': 'PVOID'},
		]
	, 'PDD_CREATEVPORTDATA': 'DD_CREATEVPORTDATA*',

	'DDCOLORCONTROL':
		[
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'lBrightness', 'type': 'LONG'},
			{'name': 'lContrast', 'type': 'LONG'},
			{'name': 'lHue', 'type': 'LONG'},
			{'name': 'lSaturation', 'type': 'LONG'},
			{'name': 'lSharpness', 'type': 'LONG'},
			{'name': 'lGamma', 'type': 'LONG'},
			{'name': 'lColorEnable', 'type': 'LONG'},
			{'name': 'dwReserved1', 'type': 'DWORD'},
		]
	, 'LPDDCOLORCONTROL': 'DDCOLORCONTROL*',

	'DD_VPORTCOLORDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpVideoPort', 'type': 'PDD_VIDEOPORT_LOCAL'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'lpColorData', 'type': 'LPDDCOLORCONTROL'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'DestroyVideoPort', 'type': 'PVOID'},
		]
	, 'PDD_VPORTCOLORDATA': 'DD_VPORTCOLORDATA*',

	'DD_CANCREATEVPORTDATA':
		[
			{'name': 'lpDD', 'type': 'PDD_DIRECTDRAW_LOCAL'},
			{'name': 'lpDDVideoPortDesc', 'type': 'LPDDVIDEOPORTDESC'},
			{'name': 'ddRVal', 'type': 'HRESULT'},
			{'name': 'CanCreateVideoPort', 'type': 'PVOID'},
		]
	, 'PDD_CANCREATEVPORTDATA': 'DD_CANCREATEVPORTDATA*',

	'LOGPALETTE':
		[
			{'name': 'palVersion', 'type': 'WORD'},
			{'name': 'palNumEntries', 'type': 'WORD'},
		]
	, 'LPLOGPALETTE': 'LOGPALETTE*',

	'CIEXYZ':
		[
			{'name': 'ciexyzX', 'type': 'FXPT2DOT30'},
			{'name': 'ciexyzY', 'type': 'FXPT2DOT30'},
			{'name': 'ciexyzZ', 'type': 'FXPT2DOT30'},
		]
	, 'LPCIEXYZ': 'CIEXYZ*',

	'CIEXYZTRIPLE':
		[
			{'name': 'ciexyzRed', 'type': 'CIEXYZ'},
			{'name': 'ciexyzGreen', 'type': 'CIEXYZ'},
			{'name': 'ciexyzBlue', 'type': 'CIEXYZ'},
		]
	, 'LPCIEXYZTRIPLE': 'CIEXYZTRIPLE*',

	'LOGCOLORSPACEW':
		[
			{'name': 'lcsSignature', 'type': 'DWORD'},
			{'name': 'lcsVersion', 'type': 'DWORD'},
			{'name': 'lcsSize', 'type': 'DWORD'},
			{'name': 'lcsCSType', 'type': 'LCSCSTYPE'},
			{'name': 'lcsIntent', 'type': 'LCSGAMUTMATCH'},
			{'name': 'lcsEndpoints', 'type': 'CIEXYZTRIPLE'},
			{'name': 'lcsGammaRed', 'type': 'DWORD'},
			{'name': 'lcsGammaGreen', 'type': 'DWORD'},
			{'name': 'lcsGammaBlue', 'type': 'DWORD'},
			{'name': 'lcsFilename', 'type': 'WCHAR', 'array': 260},
		]
	, 'LPLOGCOLORSPACEW': 'LOGCOLORSPACEW*',

	'LOGCOLORSPACEEXW':
		[
			{'name': 'lcsColorSpace', 'type': 'LOGCOLORSPACEW'},
			{'name': 'dwFlags', 'type': 'DWORD'},
		]
	, 'PLOGCOLORSPACEEXW': 'LOGCOLORSPACEEXW*',

	'DOWNLOADDESIGNVECTOR':
		[
			{'name': 'ufiBase', 'type': 'UNIVERSAL_FONT_ID'},
			{'name': 'dv', 'type': 'DESIGNVECTOR'},
		]
	, 'LPDOWNLOADDESIGNVECTOR': 'DOWNLOADDESIGNVECTOR*',

	'LARGE_STRING':
		[
			{'name': 'Length', 'type': 'ULONG', 'values': range(2, 0xFFFE, 2)},
			{'name': 'MaximumLength', 'type': 'ULONG'},
			{'name': 'Buffer', 'type': 'PVOID'},
		]
	, 'PLARGE_STRING': 'LARGE_STRING*',

	'ACCEL':
		[
			{'name': 'fVirt', 'type': 'BYTE'},
			{'name': 'key', 'type': 'WORD'},
			{'name': 'cmd', 'type': 'WORD'},
		]
	, 'LPACCEL': 'ACCEL*',

	'MSG':
		[
			{'name': 'hwnd', 'type': 'HWND'},
			{'name': 'message', 'type': 'UINT'},
			{'name': 'wParam', 'type': 'WPARAM'},
			{'name': 'lParam', 'type': 'LPARAM'},
			{'name': 'time', 'type': 'DWORD'},
			{'name': 'pt', 'type': 'POINT'},
		]
	, 'LPMSG': 'MSG*',

	'TITLEBARINFO':
		[
			{'name': 'cbSize', 'type': 'DWORD'},
			{'name': 'rcTitleBar', 'type': 'RECT'},
			{'name': 'rgstate', 'type': 'DWORD', 'array': 6},
		]
	, 'PTITLEBARINFO': 'TITLEBARINFO*',

	'PAINTSTRUCT':
		[
			{'name': 'hdc', 'type': 'HDC'},
			{'name': 'fErase', 'type': 'BOOL'},
			{'name': 'rcPaint', 'type': 'RECT'},
			{'name': 'fRestore', 'type': 'BOOL'},
			{'name': 'fIncUpdate', 'type': 'BOOL'},
			{'name': 'rgbReserved', 'type': 'BYTE', 'array': 32},
		]
	, 'PPAINTSTRUCT': 'PAINTSTRUCT*',

	'SCROLLBARINFO':
		[
			{'name': 'cbSize', 'type': 'DWORD'},
			{'name': 'rcScrollBar', 'type': 'RECT'},
			{'name': 'dxyLineButton', 'type': 'INT'},
			{'name': 'xyThumbTop', 'type': 'INT'},
			{'name': 'xyThumbBottom', 'type': 'INT'},
			{'name': 'reserved', 'type': 'INT'},
			{'name': 'rgstate', 'type': 'DWORD', 'array': 6},
		]
	, 'PSCROLLBARINFO': 'SCROLLBARINFO*',

	'MOUSEMOVEPOINT':
		[
			{'name': 'x', 'type': 'INT'},
			{'name': 'y', 'type': 'INT'},
			{'name': 'time', 'type': 'DWORD'},
			{'name': 'dwExtraInfo', 'type': 'ULONG_PTR'},
		]
	, 'LPMOUSEMOVEPOINT': 'MOUSEMOVEPOINT*',

	'RAWINPUTHEADER':
		[
			{'name': 'dwType', 'type': 'DWORD'},
			{'name': 'dwSize', 'type': 'DWORD'},
			{'name': 'hDevice', 'type': 'HANDLE'},
			{'name': 'wParam', 'type': 'WPARAM'},
		]
	, 'PRAWINPUTHEADER': 'RAWINPUTHEADER*',

	'RAWMOUSE':
		[
			{'name': 'usFlags', 'type': 'USHORT'},
			{'name': 'ulButtons', 'type': 'ULONG'},
			{'name': 'ulRawButtons', 'type': 'ULONG'},
			{'name': 'lLastX', 'type': 'LONG'},
			{'name': 'lLastY', 'type': 'LONG'},
			{'name': 'ulExtraInformation', 'type': 'ULONG'},
		]
	, 'PRAWMOUSE': 'RAWMOUSE*',

	'RAWINPUT':
		[
			{'name': 'header', 'type': 'RAWINPUTHEADER'},
			{'name': 'mouse', 'type': 'RAWMOUSE'},
		]
	, 'PRAWINPUT': 'RAWINPUT*',

	'RAWINPUTDEVICE':
		[
			{'name': 'usUsagePage', 'type': 'USHORT'},
			{'name': 'usUsage', 'type': 'USHORT'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'hwndTarget', 'type': 'HWND'},
		]
	, 'PRAWINPUTDEVICE': 'RAWINPUTDEVICE*',

	'RAWINPUTDEVICELIST':
		[
			{'name': 'hDevice', 'type': 'HANDLE'},
			{'name': 'dwType', 'type': 'DWORD'},
		]
	, 'PRAWINPUTDEVICELIST': 'RAWINPUTDEVICELIST*',

	'WINDOWPLACEMENT':
		[
			{'name': 'length', 'type': 'UINT'},
			{'name': 'flags', 'type': 'UINT'},
			{'name': 'showCmd', 'type': 'UINT'},
			{'name': 'ptMinPosition', 'type': 'POINT'},
			{'name': 'ptMaxPosition', 'type': 'POINT'},
			{'name': 'rcNormalPosition', 'type': 'RECT'},
		]
	, 'PWINDOWPLACEMENT': 'WINDOWPLACEMENT*',

	'MSG':
		[
			{'name': 'hwnd', 'type': 'HWND'},
			{'name': 'message', 'type': 'UINT'},
			{'name': 'wParam', 'type': 'WPARAM'},
			{'name': 'lParam', 'type': 'LPARAM'},
			{'name': 'time', 'type': 'DWORD'},
			{'name': 'pt', 'type': 'POINT'},
		]
	, 'PMSG': 'MSG*',

	'MENUBARINFO':
		[
			{'name': 'cbSize', 'type': 'DWORD'},
			{'name': 'rcBar', 'type': 'RECT'},
			{'name': 'hMenu', 'type': 'HMENU'},
			{'name': 'hwndMenu', 'type': 'HWND'},
			{'name': 'fFocused_and_fBarFocused', 'type': 'BOOL'},
		]
	, 'PMENUBARINFO': 'MENUBARINFO*',

	'CURSORINFO':
		[
			{'name': 'cbSize', 'type': 'DWORD'},
			{'name': 'flags', 'type': 'DWORD'},
			{'name': 'hCursor', 'type': 'HCURSOR'},
			{'name': 'ptScreenPos', 'type': 'POINT'},
		]
	, 'PCURSORINFO': 'CURSORINFO*',

	'COMBOBOXINFO':
		[
			{'name': 'cbSize', 'type': 'DWORD'},
			{'name': 'rcItem', 'type': 'RECT'},
			{'name': 'rcButton', 'type': 'RECT'},
			{'name': 'stateButton', 'type': 'DWORD'},
			{'name': 'hwndCombo', 'type': 'HWND'},
			{'name': 'hwndItem', 'type': 'HWND'},
			{'name': 'hwndList', 'type': 'HWND'},
		]
	, 'PCOMBOBOXINFO': 'COMBOBOXINFO*',

	'GETCLIPBDATA':
		[
			{'name': 'uFmtRet', 'type': 'UINT'},
			{'name': 'fGlobalHandle', 'type': 'BOOL'},
			{'name': 'handle', 'type': 'HANDLE'},
		]
	, 'PGETCLIPBDATA': 'GETCLIPBDATA*',

	'GUITHREADINFO':
		[
			{'name': 'cbSize', 'type': 'DWORD'},
			{'name': 'flags', 'type': 'DWORD'},
			{'name': 'hwndActive', 'type': 'HWND'},
			{'name': 'hwndFocus', 'type': 'HWND'},
			{'name': 'hwndCapture', 'type': 'HWND'},
			{'name': 'hwndMenuOwner', 'type': 'HWND'},
			{'name': 'hwndMoveSize', 'type': 'HWND'},
			{'name': 'hwndCaret', 'type': 'HWND'},
			{'name': 'rcCaret', 'type': 'RECT'},
		]
	, 'LPGUITHREADINFO': 'GUITHREADINFO*',

	'IMEINFO':
		[
			{'name': 'dwPrivateDataSize', 'type': 'DWORD'},
			{'name': 'fdwProperty', 'type': 'DWORD'},
			{'name': 'fdwConversionCaps', 'type': 'DWORD'},
			{'name': 'fdwSentenceCaps', 'type': 'DWORD'},
			{'name': 'fdwUICaps', 'type': 'DWORD'},
			{'name': 'fdwSCSCaps', 'type': 'DWORD'},
			{'name': 'fdwSelectCaps', 'type': 'DWORD'},
		]
	, 'PIMEINFO': 'IMEINFO*',

	'IMEINFOEX':
		[
			{'name': 'hkl', 'type': 'HKL'},
			{'name': 'ImeInfo', 'type': 'IMEINFO'},
			{'name': 'wszUIClass', 'type': 'WCHAR', 'array': 16},
			{'name': 'fdwInitConvMode', 'type': 'ULONG'},
			{'name': 'fInitOpen', 'type': 'INT'},
			{'name': 'fLoadFlag', 'type': 'INT'},
			{'name': 'dwProdVersion', 'type': 'DWORD'},
			{'name': 'dwImeWinVersion', 'type': 'DWORD'},
			{'name': 'wszImeDescription', 'type': 'WCHAR', 'array': 50},
			{'name': 'wszImeFile', 'type': 'WCHAR', 'array': 80},
			{'name': 'fSysWow64Only', 'type': 'BYTE'},
		]
	, 'PIMEINFOEX': 'IMEINFOEX*',

	'DISPLAY_DEVICEW':
		[
			{'name': 'uFmtRet', 'type': 'DWORD'},
			{'name': 'uFmtRet', 'type': 'WCHAR', 'array': 32},
			{'name': 'uFmtRet', 'type': 'WCHAR', 'array': 128},
			{'name': 'uFmtRet', 'type': 'DWORD'},
			{'name': 'uFmtRet', 'type': 'WCHAR', 'array': 128},
			{'name': 'uFmtRet', 'type': 'WCHAR', 'array': 128},
		]
	, 'PDISPLAY_DEVICEW': 'DISPLAY_DEVICEW*',

	'FINDEXISTINGCURICONPARAM':
		[
			{'name': 'bIcon', 'type': 'BOOL'},
			{'name': 'cx', 'type': 'LONG'},
			{'name': 'cy', 'type': 'LONG'},
		]
	, 'PFINDEXISTINGCURICONPARAM': 'FINDEXISTINGCURICONPARAM*',

	'ALTTABINFO':
		[
			{'name': 'cbSize', 'type': 'DWORD'},
			{'name': 'cItems', 'type': 'INT'},
			{'name': 'cColumns', 'type': 'INT'},
			{'name': 'cRows', 'type': 'INT'},
			{'name': 'iColFocus', 'type': 'INT'},
			{'name': 'iRowFocus', 'type': 'INT'},
			{'name': 'cxItem', 'type': 'INT'},
			{'name': 'cyItem', 'type': 'INT'},
			{'name': 'ptStart', 'type': 'POINT'},
		]
	, 'PALTTABINFO': 'ALTTABINFO*',

	'FLASHWINFO':
		[
			{'name': 'cbSize', 'type': 'UINT'},
			{'name': 'hwnd', 'type': 'HWND'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'uCount', 'type': 'UINT'},
			{'name': 'dwTimeout', 'type': 'DWORD'},
		]
	, 'PFLASHWINFO': 'FLASHWINFO*',

	'TRACKMOUSEEVENT':
		[
			{'name': 'cbSize', 'type': 'DWORD'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'hwndTrack', 'type': 'HWND'},
			{'name': 'dwHoverTime', 'type': 'DWORD'},
		]
	, 'LPTRACKMOUSEEVENT': 'TRACKMOUSEEVENT*',

	'CMENUINFO':
		[
			{'name': 'cbSize', 'type': 'DWORD'},
			{'name': 'fMask', 'type': 'DWORD'},
			{'name': 'dwStyle', 'type': 'DWORD'},
			{'name': 'cyMax', 'type': 'UINT'},
			{'name': 'hbrBack', 'type': 'HBRUSH'},
			{'name': 'dwContextHelpID', 'type': 'DWORD'},
			{'name': 'dwMenuData', 'type': 'ULONG_PTR'},
		]
	, 'LPCMENUINFO': 'CMENUINFO*',

	'MENUITEMINFOW':
		[
			{'name': 'cbSize', 'type': 'UINT'},
			{'name': 'fMask', 'type': 'UINT'},
			{'name': 'fType', 'type': 'UINT'},
			{'name': 'fState', 'type': 'UINT'},
			{'name': 'wID', 'type': 'UINT'},
			{'name': 'hSubMenu', 'type': 'HMENU'},
			{'name': 'hbmpChecked', 'type': 'HBITMAP'},
			{'name': 'hbmpUnchecked', 'type': 'HBITMAP'},
			{'name': 'dwItemData', 'type': 'ULONG_PTR'},
			{'name': 'dwTypeData', 'type': 'LPWSTR'},
			{'name': 'cch', 'type': 'UINT'},
			{'name': 'hbmpItem', 'type': 'HBITMAP'},
		]
	, 'LPMENUITEMINFOW': 'MENUITEMINFOW*',

	'PFNCLIENT':
		[
			{'name': 'pfnScrollBarWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnTitleWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnMenuWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnDesktopWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnDefWindowProc', 'type': 'WNDPROC'},
			{'name': 'pfnMessageWindowProc', 'type': 'WNDPROC'},
			{'name': 'pfnSwitchWindowProc', 'type': 'WNDPROC'},
			{'name': 'pfnButtonWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnComboBoxWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnComboListBoxProc', 'type': 'WNDPROC'},
			{'name': 'pfnDialogWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnEditWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnListBoxWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnMDIClientWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnStaticWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnImeWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnGhostWndProc', 'type': 'WNDPROC'},
			{'name': 'pfnHkINLPCWPSTRUCT', 'type': 'WNDPROC'},
			{'name': 'pfnHkINLPCWPRETSTRUCT', 'type': 'WNDPROC'},
			{'name': 'pfnDispatchHook', 'type': 'WNDPROC'},
			{'name': 'pfnDispatchDefWindowProc', 'type': 'WNDPROC'},
			{'name': 'pfnDispatchMessage', 'type': 'WNDPROC'},
			{'name': 'pfnMDIActivateDlgProc', 'type': 'WNDPROC'},
		]
	, 'PPFNCLIENT': 'PFNCLIENT*',

	'PFNCLIENTWORKER':
		[
			{'name': 'pfnButtonWndProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnComboBoxWndProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnComboListBoxProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnDialogWndProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnEditWndProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnListBoxWndProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnMDIClientWndProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnStaticWndProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnImeWndProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnGhostWndProc', 'type': 'WNDPROC_EX'},
			{'name': 'pfnCtfHookProc', 'type': 'WNDPROC_EX'},
		]
	, 'PPFNCLIENTWORKER': 'PFNCLIENTWORKER*',

	'TPMPARAMS':
		[
			{'name': 'cbSize', 'type': 'UINT'},
			{'name': 'rcExclude', 'type': 'RECT'},
		]
	, 'LPTPMPARAMS': 'TPMPARAMS*',

	'SETCLIPBDATA':
		[
			{'name': 'fGlobalHandle', 'type': 'BOOL'},
			{'name': 'fIncSerialNumber', 'type': 'BOOL'},
		]
	, 'PSETCLIPBDATA': 'SETCLIPBDATA*',

	'ICONINFO':
		[
			{'name': 'fIcon', 'type': 'BOOL'},
			{'name': 'xHotspot', 'type': 'DWORD'},
			{'name': 'yHotspot', 'type': 'DWORD'},
			{'name': 'hbmMask', 'type': 'HBITMAP'},
			{'name': 'hbmColor', 'type': 'HBITMAP'},
		]
	, 'PICONINFO': 'ICONINFO*',

	'SURFOBJ':
		[
			{'name': 'dhsurf', 'type': 'DHSURF'},
			{'name': 'hsurf', 'type': 'HSURF'},
			{'name': 'dhpdev', 'type': 'DHPDEV'},
			{'name': 'hdev', 'type': 'HDEV'},
			{'name': 'sizlBitmap', 'type': 'SIZE'},
			{'name': 'cjBits', 'type': 'ULONG'},
			{'name': 'pvBits', 'type': 'PVOID'},
			{'name': 'pvScan0', 'type': 'PVOID'},
			{'name': 'lDelta', 'type': 'LONG'},
			{'name': 'iUniq', 'type': 'ULONG'},
			{'name': 'iBitmapFormat', 'type': 'ULONG'},
			{'name': 'iType', 'type': 'USHORT'},
			{'name': 'fjBitmap', 'type': 'USHORT'},
		]
	, 'PSURFOBJ': 'SURFOBJ*',

	'CLIPOBJ':
		[
			{'name': 'iUniq', 'type': 'ULONG'},
			{'name': 'rclBounds', 'type': 'RECTL'},
			{'name': 'iDComplexity', 'type': 'BYTE'},
			{'name': 'iFComplexity', 'type': 'BYTE'},
			{'name': 'iMode', 'type': 'BYTE'},
			{'name': 'fjOptions', 'type': 'BYTE'},
		]
	, 'PCLIPOBJ': 'CLIPOBJ*',

	'XLATEOBJ':
		[
			{'name': 'iUniq', 'type': 'ULONG'},
			{'name': 'flXlate', 'type': 'FLONG'},
			{'name': 'iSrcType', 'type': 'USHORT'},
			{'name': 'iDstType', 'type': 'USHORT'},
			{'name': 'cEntries', 'type': 'ULONG'},
			{'name': 'pulXlate', 'type': 'PULONG'},
		]
	, 'PXLATEOBJ': 'XLATEOBJ*',

	'BRUSHOBJ':
		[
			{'name': 'iSolidColor', 'type': 'ULONG'},
			{'name': 'pvRbrush', 'type': 'PVOID'},
			{'name': 'flColorType', 'type': 'FLONG'},
		]
	, 'PBRUSHOBJ': 'BRUSHOBJ*',

	'CLSMENUNAME':
		[
			{'name': 'pszClientAnsiMenuName', 'type': 'LPSTR'},
			{'name': 'pwszClientUnicodeMenuName', 'type': 'LPWSTR'},
			{'name': 'pusMenuName', 'type': 'PUNICODE_STRING'},
		]
	, 'PCLSMENUNAME': 'CLSMENUNAME*',

	'MOUSEINPUT':
		[
			{'name': 'dx', 'type': 'LONG'},
			{'name': 'dy', 'type': 'LONG'},
			{'name': 'mouseData', 'type': 'DWORD'},
			{'name': 'dwFlags', 'type': 'DWORD'},
			{'name': 'time', 'type': 'DWORD'},
			{'name': 'dwExtraInfo', 'type': 'ULONG_PTR'},
		]
	, 'PMOUSEINPUT': 'MOUSEINPUT*',

	'INPUT':
		[
			{'name': 'type', 'type': 'DWORD'},
			{'name': 'mi', 'type': 'MOUSEINPUT'},
		]
	, 'LPINPUT': 'INPUT*',

	'BLENDFUNCTION':
		[
			{'name': 'BlendOp', 'type': 'BYTE'},
			{'name': 'BlendFlags', 'type': 'BYTE'},
			{'name': 'SourceConstantAlpha', 'type': 'BYTE'},
			{'name': 'AlphaFormat', 'type': 'BYTE'},
		]
	, 'PBLENDFUNCTION': 'BLENDFUNCTION*',

	'BLENDOBJ':
		[
			{'name': 'BlendFunction', 'type': 'BLENDFUNCTION'},
		]
	, 'PBLENDOBJ': 'BLENDOBJ*',

	'STROBJ':
		[
			{'name': 'bbbbb', 'type': 'ULONG'},
			{'name': 'bbbbb', 'type': 'FLONG'},
			{'name': 'bbbbb', 'type': 'ULONG'},
			{'name': 'bbbbb', 'type': 'RECTL'},
			{'name': 'bbbbb', 'type': 'PGLYPHPOS'},
			{'name': 'bbbbb', 'type': 'LPWSTR'},
		]
	, 'PSTROBJ': 'STROBJ*',

	'FONTOBJ':
		[
			{'name': 'iUniq', 'type': 'ULONG'},
			{'name': 'iFace', 'type': 'ULONG'},
			{'name': 'cxMax', 'type': 'ULONG'},
			{'name': 'flFontType', 'type': 'FLONG'},
			{'name': 'iTTUniq', 'type': 'ULONG_PTR'},
			{'name': 'iFile', 'type': 'ULONG_PTR'},
			{'name': 'sizLogResPpi', 'type': 'SIZE'},
			{'name': 'ulStyleSize', 'type': 'ULONG'},
			{'name': 'pvConsumer', 'type': 'PVOID'},
			{'name': 'pvProducer', 'type': 'PVOID'},
		]
	, 'PFONTOBJ': 'FONTOBJ*',

	'SBDATA':
		[
			{'name': 'posMin', 'type': 'INT'},
			{'name': 'posMax', 'type': 'INT'},
			{'name': 'page', 'type': 'INT'},
			{'name': 'pos', 'type': 'INT'},
		]
	, 'PSBDATA': 'SBDATA*',

	'SCROLLINFO':
		[
			{'name': 'cbSize', 'type': 'UINT'},
			{'name': 'fMask', 'type': 'UINT'},
			{'name': 'nMin', 'type': 'INT'},
			{'name': 'nMax', 'type': 'INT'},
			{'name': 'nPage', 'type': 'UINT'},
			{'name': 'nPos', 'type': 'INT'},
			{'name': 'nTrackPos', 'type': 'INT'},
		]
	, 'LPSCROLLINFO': 'SCROLLINFO*',

	'PATHOBJ':
		[
			{'name': 'fl', 'type': 'FLONG'},
			{'name': 'cCurves', 'type': 'ULONG'},
		]
	, 'PPATHOBJ': 'PATHOBJ*',

	'XFORMOBJ':
		[
			{'name': 'ulReserved', 'type': 'ULONG'},
		]
	, 'PXFORMOBJ': 'XFORMOBJ*',

	'LINEATTRS':
		[
			{'name': 'fl', 'type': 'FLONG'},
			{'name': 'iJoin', 'type': 'ULONG'},
			{'name': 'iEndCap', 'type': 'ULONG'},
			{'name': 'elWidth', 'type': 'FLOAT_LONG'},
			{'name': 'eMiterLimit', 'type': 'FLOATL'},
			{'name': 'cstyle', 'type': 'ULONG'},
			{'name': 'pstyle', 'type': 'PFLOAT_LONG'},
			{'name': 'elStyleState', 'type': 'FLOAT_LONG'},
		]
	, 'PLINEATTRS': 'LINEATTRS*',

	'GLYPHBITS':
		[
			{'name': 'ptlOrigin', 'type': 'POINTL'},
			{'name': 'sizlBitmap', 'type': 'SIZE'},
			{'name': 'aj', 'type': 'BYTE'},
		]
	, 'PGLYPHBITS': 'GLYPHBITS*',

	'GLYPHDEF':
		[
			{'name': 'hg', 'type': 'PGLYPHBITS'},
			{'name': 'ptl', 'type': 'PPATHOBJ'},
		]
	, 'PGLYPHDEF': 'GLYPHDEF*',

	'GLYPHPOS':
		[
			{'name': 'hg', 'type': 'HGLYPH'},
			{'name': 'pgdf', 'type': 'PGLYPHDEF'},
			{'name': 'ptl', 'type': 'PPOINTL'},
		]
	, 'PGLYPHPOS': 'GLYPHPOS*', 'PPGLYPHPOS': 'PGLYPHPOS*',

	'CURSORDATA':
		[
			{'name': 'lpName', 'type': 'LPWSTR'},
			{'name': 'lpModName', 'type': 'LPWSTR'},
			{'name': 'rt', 'type': 'USHORT'},
			{'name': 'dummy', 'type': 'USHORT'},
			{'name': 'CURSORF_flags', 'type': 'ULONG'},
			{'name': 'xHotspot', 'type': 'SHORT'},
			{'name': 'yHotspot', 'type': 'SHORT'},
			{'name': 'hbmMask', 'type': 'HBITMAP'},
			{'name': 'hbmColor', 'type': 'HBITMAP'},
			{'name': 'hbmAlpha', 'type': 'HBITMAP'},
			{'name': 'rcBounds', 'type': 'RECT'},
			{'name': 'hbmUserAlpha', 'type': 'HBITMAP'},
			{'name': 'bpp', 'type': 'ULONG'},
			{'name': 'cx', 'type': 'ULONG'},
			{'name': 'cy', 'type': 'ULONG'},
			{'name': 'cpcur', 'type': 'UINT'},
			{'name': 'cicur', 'type': 'UINT'},
			{'name': 'aspcur', 'type': 'PVOID'},  #TODO: Should reference PCURSORDATA
			{'name': 'aicur', 'type': 'PDWORD'},
			{'name': 'ajifRate', 'type': 'PINT'},
			{'name': 'iicur', 'type': 'UINT'},
		]
	, 'PCURSORDATA': 'CURSORDATA*',

	'CSCROLLINFO':
		[
			{'name': 'cbSize', 'type': 'UINT'},
			{'name': 'fMask', 'type': 'UINT'},
			{'name': 'nMin', 'type': 'INT'},
			{'name': 'nMax', 'type': 'INT'},
			{'name': 'nPage', 'type': 'UINT'},
			{'name': 'nPos', 'type': 'INT'},
			{'name': 'nTrackPos', 'type': 'INT'},
		]
	, 'LPCSCROLLINFO': 'CSCROLLINFO*',

	'WNDCLASSEXW':
		[
			{'name': 'cbSize', 'type': 'UINT'},
			{'name': 'style', 'type': 'UINT'},
			{'name': 'lpfnWndProc', 'type': 'WNDPROC'},
			{'name': 'cbClsExtra', 'type': 'INT'},
			{'name': 'cbWndExtra', 'type': 'INT'},
			{'name': 'hInstance', 'type': 'HINSTANCE'},
			{'name': 'hIcon', 'type': 'HICON'},
			{'name': 'hCursor', 'type': 'HCURSOR'},
			{'name': 'hbrBackground', 'type': 'HBRUSH'},
			{'name': 'lpszMenuName', 'type': 'LPCWSTR'},
			{'name': 'lpszClassName', 'type': 'LPCWSTR'},
			{'name': 'hIconSm', 'type': 'HICON'},
		]
	, 'LPWNDCLASSEXW': 'WNDCLASSEXW*',

	'POINTFIX':
		[
			{'name': 'x', 'type': 'FIX'},
			{'name': 'y', 'type': 'FIX'},
		]
	, 'PPOINTFIX': 'POINTFIX*',

	'FONTINFO':
		[
			{'name': 'cjThis', 'type': 'ULONG'},
			{'name': 'flCaps', 'type': 'FLONG'},
			{'name': 'cGlyphsSupported', 'type': 'ULONG'},
			{'name': 'cjMaxGlyph1', 'type': 'ULONG'},
			{'name': 'cjMaxGlyph4', 'type': 'ULONG'},
			{'name': 'cjMaxGlyph8', 'type': 'ULONG'},
			{'name': 'cjMaxGlyph32', 'type': 'ULONG'},
		]
	, 'PFONTINFO': 'FONTINFO*',

	'HGLYPH':
		[
			{'name': 'memRef', 'type': 'PVOID'},
		]
	, 'PHGLYPH': 'HGLYPH*',

	'POINTQF':
		[
			{'name': 'x', 'type': 'LARGE_INTEGER'},
			{'name': 'y', 'type': 'LARGE_INTEGER'},
		]
	, 'PPOINTQF': 'POINTQF*',

	'CLIPLINE':
		[
			{'name': 'ptfxA', 'type': 'POINTFIX'},
			{'name': 'ptfxB', 'type': 'POINTFIX'},
			{'name': 'lStyleState', 'type': 'LONG'},
			{'name': 'c', 'type': 'ULONG'},
		]
	, 'PCLIPLINE': 'CLIPLINE*',

	'SECURITY_ATTRIBUTES':
		[
			{'name': 'nLength', 'type': 'DWORD'},
			{'name': 'lpSecurityDescriptor', 'type': 'PVOID'},
			{'name': 'bInheritHandle', 'type': 'BOOL'},
		]
	, 'PSECURITY_ATTRIBUTES': 'SECURITY_ATTRIBUTES*',

	'PATHDATA':
		[
			{'name': 'flags', 'type': 'FLONG'},
			{'name': 'count', 'type': 'ULONG'},
			{'name': 'pptfx', 'type': 'PPOINTFIX'},
		]
	, 'PPATHDATA': 'PATHDATA*',

	'XFORML':
		[
			{'name': 'eM11', 'type': 'FLOATL'},
			{'name': 'eM12', 'type': 'FLOATL'},
			{'name': 'eM21', 'type': 'FLOATL'},
			{'name': 'eM22', 'type': 'FLOATL'},
			{'name': 'eDx', 'type': 'FLOATL'},
			{'name': 'eDy', 'type': 'FLOATL'},
		]
	, 'PXFORML': 'XFORML*',
}