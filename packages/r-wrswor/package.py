# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrswor(RPackage):
	"""Weighted Random Sampling without Replacement

	A collection of implementations of classical and
    novel algorithms for weighted sampling without replacement.
	"""
	
	homepage = "http://krlmlr.github.io/wrswoR"
	cran = "wrswoR" 

	version("1.1.1", md5="4a3e878626def56ca4991ceb38f26780")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-logging@0.4.13:", type=("build", "run"))
	depends_on("r-rcpp@0.11.5:", type=("build", "run"))
