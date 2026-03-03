# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBssasymp(RPackage):
	"""Asymptotic Covariance Matrices of Some BSS Mixing and Unmixing
Matrix Estimates

	Functions to compute the asymptotic covariance matrices of mixing and unmixing matrix estimates of the following blind source separation (BSS) methods: symmetric and squared symmetric FastICA, regular and adaptive deflation-based FastICA, FOBI, JADE, AMUSE and deflation-based and symmetric SOBI. Also functions to estimate these covariances based on data are available. 
	"""
	
	cran = "BSSasymp" 

	version("1.2-3", md5="e665a299ef8fd61a3fe6737d71456e45")

	depends_on("r-fica@1.0.2:", type=("build", "run"))
	depends_on("r-jade", type=("build", "run"))
