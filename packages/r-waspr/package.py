# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaspr(RPackage):
	"""Wasserstein Barycenters of Subset Posteriors

	Functions to compute Wasserstein barycenters
    of subset posteriors using the swapping algorithm developed by Puccetti, 
    Rüschendorf and Vanduffel (2020) <doi:10.1016/j.jmaa.2017.02.003>. The 
    Wasserstein barycenter is a geometric approach for combining subset 
    posteriors. It allows for parallel and distributed computation of the 
    posterior in case of complex models and/or big datasets, thereby increasing
    computational speed tremendously.
	"""
	
	homepage = "https://github.com/joliencremers/waspr"
	cran = "waspr" 

	version("1.0.1", md5="6409a805b8165c620bc75c0d494a54e2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
