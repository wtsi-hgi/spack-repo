# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNppbib(RPackage):
	"""Nonparametric Partially-Balanced Incomplete Block Design
Analysis

	Implements a nonparametric statistical test for rank or score data
 from partially-balanced incomplete block-design experiments.
	"""
	
	homepage = "https://github.com/dalling1"
	cran = "nppbib" 

	version("1.2-0", md5="339ac777ca578c70727ab1417761cadd")

