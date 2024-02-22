# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwcrtdesign(RPackage):
	"""Stepped Wedge Cluster Randomized Trial (SW CRT) Design

	A set of tools for examining the design and analysis aspects of stepped wedge cluster randomized trials (SW CRT) based on a repeated cross-sectional sampling scheme (Hussey MA and Hughes JP (2007) Contemporary Clinical Trials 28:182-191. <doi:10.1016/j.cct.2006.05.007>). 
	"""
	
	cran = "swCRTdesign" 

	version("4.0", md5="c8eb2ee8389f33c5268d12773419a94c")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
