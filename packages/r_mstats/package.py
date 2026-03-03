# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstats(RPackage):
	"""Epidemiological Data Analysis

	This is a tool for epidemiologist, medical data analyst, 
    medical or public health professionals. It contains three domains of functions:
    1) data management, 2) statistical analysis and 3) calculating 
    epidemiological measures.
	"""
	
	homepage = "https://myominnoo.github.io/"
	cran = "mStats" 

	version("3.4.0", md5="72548d39557984263fa701b11cafe2c6")

	depends_on("r@4:", type=("build", "run"))
