# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLvgp(RPackage):
	"""Latent Variable Gaussian Process Modeling with Qualitative and
Quantitative Input Variables

	Fit response surfaces for datasets with latent-variable Gaussian process modeling, predict responses for new inputs, and plot latent variables locations in the latent space (only 1D or 2D).
    The input variables of the datasets can be quantitative, qualitative/categorical or mixed.
    The output variable of the datasets is a scalar (quantitative).
    The optimization of the likelihood function is done using a successive approximation/relaxation algorithm similar to another GP modeling package "GPM".
    The modeling method is published in "A Latent Variable Approach to Gaussian Process Modeling with Qualitative and Quantitative Factors"
    by Yichi Zhang, Siyu Tao, Wei Chen, and Daniel W. Apley (2018) <arXiv:1806.07504>. The package is developed in IDEAL of Northwestern University.
	"""
	
	cran = "LVGP" 

	version("2.1.5", md5="4df3f1439a61063c71a7f9e455a1f4d5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lhs@0.14:", type=("build", "run"))
	depends_on("r-randtoolbox@1.17:", type=("build", "run"))
