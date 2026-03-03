# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimalsurrogate(RPackage):
	"""Model Free Approach to Quantifying Surrogacy

	Identifies an optimal transformation of a surrogate marker such that the proportion of treatment effect explained can be inferred based on the transformation of the surrogate and nonparametrically estimates two model-free quantities of this proportion. Details are described in Wang et al (2020) <doi:10.1093/biomet/asz065>.    
	"""
	
	cran = "OptimalSurrogate" 

	version("1.0", md5="83d12e2b00508b2f624a2be7a8d0263a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
