# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonparametricBayes(RPackage):
	"""Project Code - Nonparametric Bayes

	Basic implementation of a Gibbs sampler for a Chinese Restaurant Process along with some visual aids to help understand how the sampling works. This is developed as part of a postgraduate school project for an Advanced Bayesian Nonparametric course. It is inspired by Tamara Broderick's presentation on Nonparametric Bayesian statistics given at the Simons institute.
	"""
	
	cran = "nonparametric.bayes" 

	version("0.0.1", md5="9a64e5fe61a5ab8e2ef8da18916d82c2")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
