# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocatexec(RPackage):
	"""Detection and Localization of Executable Files

	A set of functions to locate some programs 
 available on the user machine. The package provides functions to locate 
 'Node.js', 'npm', 'LibreOffice', 'Microsoft Word', 'Microsoft PowerPoint', 
 'Microsoft Excel', 'Python', 'pip', 'Mozilla Firefox' and 'Google Chrome'.
 User can test the availability of a program with eventually a version 
 and call it with function system2() or system(). This allows the use of 
 a single function to retrieve the path to a program regardless of the 
 operating system and its configuration.
	"""
	
	cran = "locatexec" 

	version("0.1.1", md5="ead1f832f49a6ca9b23bbfdcefdc005a")

