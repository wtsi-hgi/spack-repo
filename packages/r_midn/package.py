# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidn(RPackage):
	"""Nearly Exact Sample Size Calculation for Exact Powerful
Nonrandomized Tests for Differences Between Binomial
Proportions

	Implementation of the mid-n algorithms presented in 
             Wellek S (2015) <DOI:10.1111/stan.12063> Statistica Neerlandica 69, 358-373 for exact 
             sample size calculation for superiority trials with binary outcome.
	"""
	
	cran = "MIDN" 

	version("1.0", md5="4a3492a8fcad11bc56512b43fa79acef")

	depends_on("r-biasedurn", type=("build", "run"))
