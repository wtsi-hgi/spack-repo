# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlakeanalyzer(RPackage):
	"""Lake Physics Tools

	Standardized methods for calculating common important derived
    physical features of lakes including water density based based on
    temperature, thermal layers, thermocline depth, lake number, Wedderburn
    number, Schmidt stability and others.
	"""
	
	cran = "rLakeAnalyzer" 

	version("1.11.4.1", md5="cf43f237eec5ceec4821a9e832c70bc0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
