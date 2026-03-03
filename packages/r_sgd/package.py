# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgd(RPackage):
	"""Stochastic Gradient Descent for Scalable Estimation

	A fast and flexible set of tools for large scale estimation. It
    features many stochastic gradient methods, built-in models, visualization
    tools, automated hyperparameter tuning, model checking, interval estimation,
    and convergence diagnostics.
	"""
	
	homepage = "https://github.com/airoldilab/sgd"
	cran = "sgd" 

	version("1.1.2", md5="e6615005fbf62948d489f526d34ea585")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
