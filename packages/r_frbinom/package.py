# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrbinom(RPackage):
	"""Fractional Binomial Distributions

	Generating fractional binomial random variables and computing density, cumulative distribution, and quantiles of fractional binomial distributions. (Lee, J. (2023) <arXiv:2209.01516>.)
	"""
	
	cran = "frbinom" 

	version("1.0.0", md5="7fd5307711db13018da714a873400003")

