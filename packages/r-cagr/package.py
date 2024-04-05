# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCagr(RPackage):
	"""Compound Annual Growth Rate

	A time series usually does not have a uniform growth rate. Compound Annual Growth Rate measures the average annual growth over a given period. More details can be found in Bardhan et al. (2022) <DOI:10.18805/ag.D-5418>.
	"""
	
	cran = "CAGR" 

	version("1.1.0", md5="3ed18257b09dd1f0cfb324d0f6a1925b")
	version("0.1.0", md5="981126ab61ee1f318d0518d58fa3a7fc")

