# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBssoverspace(RPackage):
	"""Blind Source Separation for Multivariate Spatial Data using
Eigen Analysis

	Provides functions for blind source separation over multivariate spatial data, and useful statistics for evaluating performance of estimation on mixing matrix. 'BSSoverSpace' is based on an eigen analysis of a positive definite matrix defined in terms of multiple normalized spatial local covariance matrices, and thus can handle moderately high-dimensional random fields. This package is an implementation of the method described in Zhang, Hao and Yao (2022)<arXiv:2201.02023>.
	"""
	
	cran = "BSSoverSpace" 

	version("0.1.0", md5="62230a9115f78c25bd897f37cb82db10")

	depends_on("r-spatialbss", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rspde", type=("build", "run"))
