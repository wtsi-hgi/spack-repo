# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdiftest(RPackage):
	"""Item-Wise Score-Based DIF Detection

	Detection of item-wise Differential Item Functioning (DIF) 
             in fitted 'mirt', 'multipleGroup' or 'bfactor' models  
             using score-based structural change tests. Under the hood 
             the sctest() function from the 'strucchange' package is used.
	"""
	
	cran = "scDIFtest" 

	version("0.1.1", md5="92bfe8359e6d2993c6a1762040681404")

	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
