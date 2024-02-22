# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefa(RPackage):
	"""Robust Exponential Factor Analysis

	A robust alternative to the traditional principal component estimator is proposed within the framework of factor models, known as Robust Exponential Factor Analysis, specifically designed for the modeling of high-dimensional datasets with heavy-tailed distributions. The algorithm estimates the latent factors and the loading by minimizing the exponential squared loss function. To determine the appropriate number of factors, we propose a modified rank minimization technique, which has been shown to significantly enhance finite-sample performance.  
	"""
	
	cran = "REFA" 

	version("0.1.0", md5="59c8ec5eca9ce6ef1e21702334859895")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
