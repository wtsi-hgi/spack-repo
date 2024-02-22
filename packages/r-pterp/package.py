# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPterp(RPackage):
	"""PTE and RP for Optimally-Transformed Surrogate

	Evaluates the strength of a surrogate marker by estimating the proportion of treatment effect explained (PTE) and relative power(RP) for the optimally-transformed version of the surrogate.  Details available in Wang et al (2022) <arXiv:2209.08414>. 
	"""
	
	cran = "PTERP" 

	version("1.0", md5="6cfca275e69ca345a111008eb054904d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
