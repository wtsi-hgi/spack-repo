# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwinning(RPackage):
	"""Data Twinning

	An efficient algorithm for data twinning. This work is supported by U.S. National Science 
	Foundation grants DMREF-1921873 and CMMI-1921646.
	"""
	
	cran = "twinning" 

	version("1.0", md5="4e92ccf77205fc1b4b267014a686ba93")

	depends_on("r-rcpp", type=("build", "run"))
