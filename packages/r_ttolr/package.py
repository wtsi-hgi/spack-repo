# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtolr(RPackage):
	"""Likelihood Ratio Statistics for One or Two Sample T-Tests

	Likelihood ratio and maximum likelihood statistics are provided 
     that can be used as alternatives to p-values Colquhoun (2017) 
     <doi:10.1098/rsos.171085>. Arguments can be either p-values or t-statistics. 
     together with degrees of freedom. For the function 'tTOlr', the argument
     'twoSided' has the default 'twoSided = TRUE'.
	"""
	
	cran = "tTOlr" 

	version("0.2.3", md5="7b8d27ba8511a2a0e59868e09e33fde7")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
