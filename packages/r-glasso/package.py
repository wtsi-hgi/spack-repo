# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlasso(RPackage):
	"""Graphical Lasso: Estimation of Gaussian Graphical Models

	Estimation of a sparse inverse covariance matrix using a lasso (L1)
             penalty. Facilities are provided for estimates along a path of values
	     for the regularization parameter.
	"""
	
	homepage = "http://www-stat.stanford.edu/~tibs/glasso"
	cran = "glasso" 

	version("1.11", md5="f0b42c09df8d4845624821cb2d017f45")

