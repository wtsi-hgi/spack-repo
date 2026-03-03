# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorpreave(RPackage):
	"""Rank and Factor Loadings Estimation in Time Series Tensor Factor
Models

	A set of functions to estimate rank and factor loadings of time series tensor factor models. A tensor is a multidimensional array. To analyze high-dimensional tensor time series, factor model is a major dimension reduction tool. 'TensorPreAve' provides functions to estimate the rank of core tensors and factor loading spaces of tensor time series. More specifically, a pre-averaging method that accumulates information from tensor fibres is used to estimate the factor loading spaces. The estimated directions corresponding to the strongest factors are then used for projecting the data for a potentially improved re-estimation of the factor loading spaces themselves. A new rank estimation method is also implemented to utilizes correlation information from the projected data. 
    See Chen and Lam (2023) <arXiv:2208.04012> for more details.
	"""
	
	homepage = "https://github.com/William-Chenwl/TensorPreAve"
	cran = "TensorPreAve" 

	version("1.1.0", md5="4058399efc647b30c7c472e413a311b3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
