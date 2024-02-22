# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpev(RPackage):
	"""Unsmoothed and Smoothed Penalized PCA using Nesterov Smoothing

	We provide functionality to implement penalized PCA with an option to smooth the objective function using Nesterov smoothing. Two functions are available to compute a user-specified number of eigenvectors. The function unsmoothed_penalized_EV() computes a penalized PCA without smoothing and has three parameters (the input matrix, the Lasso penalty, and the number of desired eigenvectors). The function smoothed_penalized_EV() computes a smoothed penalized PCA using the same parameters and additionally requires the specification of a smoothing parameter. Both functions return a matrix having the desired eigenvectors as columns.
	"""
	
	cran = "SPEV" 

	version("1.0.0", md5="cdcb2e8c0560658843d17170f4bb6855")

