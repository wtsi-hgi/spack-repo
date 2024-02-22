# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantdr(RPackage):
	"""Dimension Reduction Techniques for Conditional Quantiles

	An implementation of dimension reduction techniques
    for conditional quantiles. Nonparametric estimation of 
    conditional quantiles is also available.  
	"""
	
	homepage = "https://github.com/elianachristou/quantdr"
	cran = "quantdr" 

	version("1.2.2", md5="ce9ece50c3956ff5e99b818cf023a420")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dr", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
