# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLakemetabolizer(RPackage):
	"""Tools for the Analysis of Ecosystem Metabolism

	A collection of tools for the calculation of freewater metabolism
    from in situ time series of dissolved oxygen, water temperature, and,
    optionally, additional environmental variables. LakeMetabolizer implements
    5 different metabolism models with diverse statistical underpinnings:
    bookkeeping, ordinary least squares, maximum likelihood, Kalman filter,
    and Bayesian. Each of these 5 metabolism models can be combined with
    1 of 7 models for computing the coefficient of gas exchange across the
    air–water interface (k). LakeMetabolizer also features a variety of
    supporting functions that compute conversions and implement calculations
    commonly applied to raw data prior to estimating metabolism (e.g., oxygen
    saturation and optical conversion models).
	"""
	
	homepage = "https://www.tandfonline.com/doi/abs/10.1080/IW-6.4.883"
	cran = "LakeMetabolizer" 

	version("1.5.5", md5="991d96abd92608108ced4f276db6abc3")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rlakeanalyzer@1.4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
