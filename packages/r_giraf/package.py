# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGiraf(RPackage):
	"""Gibbs Random Fields Analysis

	Allows calculation on, and
 sampling from Gibbs Random Fields, and more precisely general 
 homogeneous Potts model. The primary tool is the exact computation of
 the intractable normalising constant for small rectangular lattices. 
 Beside the latter function, it contains method that give exact sample from the likelihood
 for small enough rectangular lattices or approximate sample from the 
 likelihood using MCMC samplers for large lattices.
	"""
	
	cran = "GiRaF" 

	version("1.0.1", md5="1551624d61798cad5f94e251b4e2e10e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
