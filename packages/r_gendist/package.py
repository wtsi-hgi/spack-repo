# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGendist(RPackage):
	"""Generated Probability Distribution Models

	Computes the probability density function (pdf), cumulative distribution function (cdf), quantile function (qf) and generates random values (rg) for the following general models : mixture models, composite models, folded models, skewed symmetric models and arc tan models.
	"""
	
	cran = "gendist" 

	version("2.0", md5="6f92ae3e87cf64647afcd3ac88a74b32")

