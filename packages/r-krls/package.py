# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKrls(RPackage):
	"""Kernel-Based Regularized Least Squares

	Package implements Kernel-based Regularized Least Squares (KRLS), a machine learning method to fit multidimensional functions y=f(x) for regression and classification problems without relying on linearity or additivity assumptions. KRLS finds the best fitting function by minimizing the squared loss of a Tikhonov regularization problem, using Gaussian kernels as radial basis functions. For further details see Hainmueller and Hazlett (2014).
	"""
	
	homepage = "https://www.r-project.org"
	cran = "KRLS" 

	version("1.0-0", md5="0ba21c2428ae9ef0991d652e260fdc3c")

