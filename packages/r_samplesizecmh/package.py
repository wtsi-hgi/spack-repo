# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplesizecmh(RPackage):
	"""Power and Sample Size Calculation for the
Cochran-Mantel-Haenszel Test

	
    Calculates the power and sample size for Cochran-Mantel-Haenszel tests. 
    There are also several helper functions for working with probability,
    odds, relative risk, and odds ratio values.
	"""
	
	homepage = "https://github.com/pegeler/samplesizeCMH"
	cran = "samplesizeCMH" 

	version("0.0.3", md5="87ad770804e015c820bd882ef36694a8")

	depends_on("r@3.4:", type=("build", "run"))
