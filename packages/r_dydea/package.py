# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDydea(RPackage):
	"""Detection of Chaotic and Regular Intervals in the Data

	Finds regular and chaotic intervals in the data using 
    the 0-1 test for chaos proposed by Gottwald and Melbourne (2004) 
	<DOI:10.1137/080718851>. 
	"""
	
	cran = "dydea" 

	version("0.1.0", md5="b5d54195713b2d51f5ab022a9dec23f1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chaos01", type=("build", "run"))
