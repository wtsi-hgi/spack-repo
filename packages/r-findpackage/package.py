# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFindpackage(RPackage):
	"""Find 'CRAN' Package by Topic

	Finds 'CRAN' packages by the topic requested. The topic can be given as a character string or as a regular expression and will help users to locate 'CRAN' packages matching their specified requirement. findPackage(<string>) returns a data frame of packages with description containing the input string. 
	"""
	
	homepage = "<https://CRAN.R-project.org/package=findPackage>"
	cran = "findPackage" 

	version("0.2.0", md5="74e7cce0770c06623c74ec70b8419c05")

