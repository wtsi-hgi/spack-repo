# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgr(RPackage):
	"""Compound Growth Rate for Capturing the Growth Rate Over the
Period

	The compound growth rate indicates the percentage change of a specific variable over a defined period. It is calculated using non-linear models, particularly the exponential model. To estimate the compound growth rates, the growth model is first converted to semilog form and then analyzed using Ordinary Least Squares (OLS) regression. This package has been developed using concept of Shankar et al. (2022)<doi:10.3389/fsufs.2023.1208898>.
	"""
	
	cran = "CGR" 

	version("0.1.0", md5="dafb9929e8e13db17fa1fcde9037000b")

