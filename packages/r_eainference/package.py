# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REainference(RPackage):
	"""Estimator Augmentation and Simulation-Based Inference

	Estimator augmentation methods for statistical inference on high-dimensional data, 
    as described in Zhou, Q. (2014) <arXiv:1401.4425v2>
    and Zhou, Q. and Min, S. (2017) <doi:10.1214/17-EJS1309>.
    It provides several simulation-based inference methods: (a) Gaussian and 
    wild multiplier bootstrap for lasso, group lasso, scaled lasso, scaled group
    lasso and their de-biased estimators, (b) importance sampler for approximating
    p-values in these methods, (c) Markov chain Monte Carlo lasso sampler with 
    applications in post-selection inference.
	"""
	
	cran = "EAinference" 

	version("0.2.3", md5="af094b69f8a6225b9f78f10f136acbf9")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hdi", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
