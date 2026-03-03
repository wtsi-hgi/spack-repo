# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasysdctable(RPackage):
	"""Easy Interface to the Statistical Disclosure Control Package
'sdcTable' Extended with Own Implementation of
'GaussSuppression'

	The main function, ProtectTable(), performs table suppression according to a 
 frequency rule with a data set as the only required input. Within this function, 
 protectTable(), protect_linked_tables() or runArgusBatchFile() in package 'sdcTable' is called. 
 Lists of level-hierarchy (parameter 'dimList') and other required input to these functions 
 are created automatically. 
 The suppression method Gauss (default) is implemented independently of 'sdcTable'.
 The function, PTgui(), starts a graphical user interface based on the 'shiny' package.
	"""
	
	homepage = "https://github.com/statisticsnorway/easySdcTable"
	cran = "easySdcTable" 

	version("1.0.7", md5="e664cd05959720ec6d3322de9c2fdacb")

	depends_on("r-ssbtools", type=("build", "run"))
	depends_on("r-sdctable", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
