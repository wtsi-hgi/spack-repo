# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLambertw(RPackage):
	"""Probabilistic Models to Analyze and Gaussianize Heavy-Tailed,
Skewed Data

	Lambert W x F distributions are a generalized framework to analyze
    skewed, heavy-tailed data. It is based on an input/output system, where the
    output random variable (RV) Y is a non-linearly transformed version of an input
    RV X ~ F with similar properties as X, but slightly skewed (heavy-tailed).
    The transformed RV Y has a Lambert W x F distribution. This package contains
    functions to model and analyze skewed, heavy-tailed data the Lambert Way:
    simulate random samples, estimate parameters, compute quantiles, and plot/
    print results nicely. The most useful function is 'Gaussianize',
    which works similarly to 'scale', but actually makes the data Gaussian.
    A do-it-yourself toolkit allows users to define their own Lambert W x
    'MyFavoriteDistribution' and use it in their analysis right away.
	"""
	
	homepage = "https://github.com/gmgeorg/LambertW"
	cran = "LambertW" 

	version("0.6.9-1", md5="fd0171b10c38caf64db975de60a7eeae")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lamw", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
