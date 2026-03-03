# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFy(RPackage):
	"""Utilities for Financial Years

	In Australia, a financial year (or fiscal year) is the period from 1 July to 30 June
     of the following calendar year. As such, many databases need to represent and 
     validate financial years efficiently. While the use of integer years with a convention that  
     they represent the year ending is common, it may lead to ambiguity with calendar years.
     On the other hand, string representations may be too inefficient and do not easily admit
     arithmetic operations. This package tries to make validation of financial years quicker while
     retaining clarity.
	"""
	
	cran = "fy" 

	version("0.4.2", md5="7a56a57dcd3e326e405cfb6a3037492b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hutils", type=("build", "run"))
