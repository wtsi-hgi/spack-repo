# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoltzmm(RPackage):
	"""Boltzmann Machines with MM Algorithms

	Provides probability computation, data generation,
    and model estimation for fully-visible Boltzmann machines. It follows the methods
    described in Nguyen and Wood (2016a) <doi:10.1162/NECO_a_00813> 
    and Nguyen and Wood (2016b) <doi:10.1109/TNNLS.2015.2425898>. 
	"""
	
	cran = "BoltzMM" 

	version("0.1.4", md5="23e96d87521f2e90d4b01b0324ff7a81")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
