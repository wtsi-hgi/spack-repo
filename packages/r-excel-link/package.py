# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcelLink(RPackage):
	"""Convenient Data Exchange with Microsoft Excel

	Allows access to data in running instance of Microsoft Excel
    (e. g. 'xl[a1] = xl[b2]*3' and so on). Graphics can be transferred with
    'xl[a1] = current.graphics()'. Additionally there are function for reading/writing 
    'Excel' files - 'xl.read.file'/'xl.save.file'. They are not fast but able to read/write 
    '*.xlsb'-files and password-protected files. There is an Excel workbook with 
    examples of calling R from Excel in the 'doc' folder. It tries to keep things as
    simple as possible - there are no needs in any additional
    installations besides R, only 'VBA' code in the Excel workbook.
    Microsoft Excel is required for this package.
	"""
	
	homepage = "https://github.com/gdemin/excel.link"
	cran = "excel.link" 

	version("0.9.12", md5="7cff570d87beb999be322fdcb1c0b55c")

