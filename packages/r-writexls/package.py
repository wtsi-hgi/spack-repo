# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RWritexls(RPackage):
	"""Cross-Platform Perl Based R Function to Create Excel 2003 (XLS)
and Excel 2007 (XLSX) Files

	Cross-platform Perl based R function to create Excel 2003 (XLS) and Excel 2007 (XLSX)
             files from one or more data frames. Each data frame will be
             written to a separate named worksheet in the Excel spreadsheet.
             The worksheet name will be the name of the data frame it contains
             or can be specified by the user. 
	"""
	
	homepage = "https://github.com/marcschwartz/WriteXLS"
	cran = "WriteXLS" 

	version("6.4.0", md5="b62412fab12ed7ffa5f47ed4238cdb15")


