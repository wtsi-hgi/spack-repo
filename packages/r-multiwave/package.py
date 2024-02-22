# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiwave(RPackage):
	"""Estimation of Multivariate Long-Memory Models Parameters

	Computation of an estimation of the long-memory parameters and
     the long-run covariance matrix using a multivariate model
	 (Lobato (1999) <doi:10.1016/S0304-4076(98)00038-4>; Shimotsu (2007) <doi:10.1016/j.jeconom.2006.01.003>). Two semi-parametric methods are
	 implemented: a Fourier based approach (Shimotsu (2007) <doi:10.1016/j.jeconom.2006.01.003>) and a wavelet based
	 approach (Achard and Gannaz (2016) <doi:10.1111/jtsa.12170>).
	"""
	
	cran = "multiwave" 

	version("1.4", md5="0ba6c6db7417241dfa044674b7f3ee5b")

