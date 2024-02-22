# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrcarlate(RPackage):
	"""Improving Estimation Efficiency in CAR with Imperfect Compliance

	We provide a list of functions for replicating the results of the Monte Carlo simulations and empirical application of Jiang et al. (2022). 
    In particular, we provide corresponding functions for generating the three types of random data described in this paper, as well as all the estimation strategies. 
    Detailed information about the data generation process and estimation strategy can be found in Jiang et al. (2022)  <doi:10.48550/arXiv.2201.13004>.
	"""
	
	cran = "drcarlate" 

	version("1.2.0", md5="65d7968e3e027b6ea642da75df318ee2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-splus2r", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
