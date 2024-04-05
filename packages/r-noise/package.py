# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoise(RPackage):
	"""Estimation of Intrinsic and Extrinsic Noise from Single-Cell
Data

	Functions to calculate estimates of intrinsic and extrinsic noise from the two-reporter single-cell experiment, as in Elowitz, M. B., A. J. Levine, E. D. Siggia, and P. S. Swain (2002) Stochastic gene expression in a single cell. Science, 297, 1183-1186.  Functions implement multiple estimators developed for unbiasedness or min Mean Squared Error (MSE) in Fu, A. Q. and Pachter, L. (2016). Estimating intrinsic and extrinsic noise from single-cell gene expression measurements. Statistical Applications in Genetics and Molecular Biology, 15(6), 447-471.
	"""
	
	cran = "noise" 

	version("1.0.2", md5="676c0af221050757140bbf4b5263d653")
	version("1.0.1", md5="bb8829fc91c21c0ce89cb904bbbd7744")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
