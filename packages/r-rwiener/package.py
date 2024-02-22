# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwiener(RPackage):
	"""Wiener Process Distribution Functions

	Provides Wiener process distribution functions,
  namely the Wiener first passage time density, CDF, quantile and random
  functions. Additionally supplies a modelling function (wdm) and further
  methods for the resulting object.
	"""
	
	homepage = "https://github.com/yeagle/RWiener"
	cran = "RWiener" 

	version("1.3-3", md5="06e3a50ce4d4ba1592c1e24e33b9cc7d")

	depends_on("r@3:", type=("build", "run"))
