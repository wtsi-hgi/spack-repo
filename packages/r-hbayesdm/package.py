# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHbayesdm(RPackage):
	"""Hierarchical Bayesian Modeling of Decision-Making Tasks

	
    Fit an array of decision-making tasks with computational models in
    a hierarchical Bayesian framework. Can perform hierarchical Bayesian analysis of
    various computational models with a single line of coding
    (Ahn et al., 2017) <doi:10.1162/CPSY_a_00002>.
	"""
	
	homepage = "https://github.com/CCS-Lab/hBayesDM"
	cran = "hBayesDM" 

	version("1.2.1", md5="0b9753bca11f8a3875c82ca1af476d34")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
