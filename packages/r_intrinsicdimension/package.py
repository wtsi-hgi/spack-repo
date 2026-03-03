# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntrinsicdimension(RPackage):
	"""Intrinsic Dimension Estimation

	A variety of methods for estimating intrinsic dimension of data sets (i.e the manifold or Hausdorff dimension of the support of the distribution that generated the data) as reviewed in Johnsson, K. (2016, ISBN:978-91-7623-921-6) and Johnsson, K., Soneson, C. and Fontes, M. (2015) <doi:10.1109/TPAMI.2014.2343220>. Furthermore, to evaluate the performance of these estimators, functions for generating data sets with given intrinsic dimensions are provided.
	"""
	
	cran = "intrinsicDimension" 

	version("1.2.0", md5="ec5e20e650021dc60b13ef571c2ea4d4")

	depends_on("r-yaimpute", type=("build", "run"))
