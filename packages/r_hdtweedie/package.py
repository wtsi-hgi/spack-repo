# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdtweedie(RPackage):
	"""The Lasso for Tweedie's Compound Poisson Model Using an IRLS-BMD
Algorithm

	The Tweedie lasso model implements an iteratively reweighed least square (IRLS) strategy that incorporates a blockwise majorization decent (BMD) method, for efficiently computing solution paths of the (grouped) lasso and the (grouped) elastic net methods.
	"""
	
	cran = "HDtweedie" 

	version("1.2", md5="f420852f3b59c2ed621088e3d8496fb1")

