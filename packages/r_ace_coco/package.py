# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAceCoco(RPackage):
	"""Analysis of Correlated High-Dimensional Expression (ACE) Data

	A function for estimating factor models. Give factor-adjusted statistics, 
  factor-adjusted mean estimation (one-sample test) or factor-adjusted mean difference 
  estimation (two-sample test).
	"""
	
	homepage = "https://github.com/hongyuan-cao/ACE"
	cran = "ACE.CoCo" 

	version("0.1", md5="437daef4cbf827c828a499eb5d3843fc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
