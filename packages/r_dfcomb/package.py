# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfcomb(RPackage):
	"""Phase I/II Adaptive Dose-Finding Design for Combination Studies

	Phase I/II adaptive dose-finding design for combination
   studies where toxicity rates are supposed to increase with both agents.
	"""
	
	cran = "dfcomb" 

	version("3.1-1", md5="cead7e883d3e633d3904827244b72c12")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-bh@1.55:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress@0.2.1:", type=("build", "run"))
