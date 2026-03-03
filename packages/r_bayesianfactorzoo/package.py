# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianfactorzoo(RPackage):
	"""Bayesian Solutions for the Factor Zoo: We Just Ran Two
Quadrillion Models

	Contains the functions to use the econometric methods in the paper Bryzgalova, Huang, and Julliard (2023) <doi:10.1111/jofi.13197>. In this package, we provide a novel Bayesian framework for analyzing linear asset pricing models: simple, robust, and applicable to high-dimensional problems. For a stand-alone model, we provide functions including BayesianFM() and BayesianSDF() to deliver reliable price of risk estimates for both tradable and nontradable factors. For competing factors and possibly nonnested models, we provide functions including continuous_ss_sdf(), continuous_ss_sdf_v2(), and dirac_ss_sdf_pvalue() to analyze high-dimensional models. If you use this package, please cite the paper. We are thankful to Yunan Ding and Jingtong Zhang for their research assistance. Any errors or omissions are the responsibility of the authors.
	"""
	
	cran = "BayesianFactorZoo" 

	version("0.0.0.2", md5="a6f17724637342c9ea6a72e6ff134aa2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nse", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
