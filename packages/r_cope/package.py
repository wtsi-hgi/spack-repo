# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCope(RPackage):
	"""Coverage Probability Excursion (CoPE) Sets

	Provides functions to  compute and plot Coverage
    Probability Excursion (CoPE) sets
    for real valued functions on a 2-dimensional domain. CoPE sets are obtained
    from repeated noisy observations of the function on the entire domain.
    They are designed to bound the excursion
    set of the target function at a given level from above and below with
    a predefined probability. The target
    function can be a parameter in spatially-indexed linear regression.
    Support by NIH grant R01 CA157528 is gratefully acknowledged. 
	"""
	
	cran = "cope" 

	version("0.2.3", md5="f55f70a9c7ca002371dcfb029ea159f3")

	depends_on("r-maps@2.3.7:", type=("build", "run"))
	depends_on("r-abind@1.4.3:", type=("build", "run"))
	depends_on("r-fields@7.1:", type=("build", "run"))
	depends_on("r-mass@7.3.34:", type=("build", "run"))
	depends_on("r-matrix@1.2.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.0:", type=("build", "run"))
	depends_on("r-nlme@3.1.122:", type=("build", "run"))
