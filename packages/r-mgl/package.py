# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgl(RPackage):
	"""Module Graphical Lasso

	An aggressive dimensionality reduction and network estimation
    technique for a high-dimensional Gaussian graphical model (GGM). Please
    refer to: Efficient Dimensionality Reduction for High-Dimensional Network
    Estimation, Safiye Celik, Benjamin A. Logsdon, Su-In Lee, Proceedings of
    The 31st International Conference on Machine Learning, 2014, p. 1953--1961.
	"""
	
	homepage = "https://sites.google.com/a/cs.washington.edu/mgl/"
	cran = "MGL" 

	version("1.1", md5="be5aa08871551b827779907bb5d5ff8f")

