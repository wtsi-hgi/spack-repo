# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatest(RPackage):
	"""Score Test and Meta-Analysis Based on Saddlepoint Approximation

	Performs score test using saddlepoint approximation to estimate the null distribution. Also prepares summary statistics for meta-analysis and performs meta-analysis to combine multiple association results. For the latest version, please check <https://github.com/leeshawn/SPAtest>.
	"""
	
	cran = "SPAtest" 

	version("3.1.2", md5="4f4e924f56bf00483c5bc545494016b3")

	depends_on("r@3:", type=("build", "run"))
