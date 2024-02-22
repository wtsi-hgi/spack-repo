# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNemtr(RPackage):
	"""Nonparametric Extended Median Test - Cumulative Summation Method

	Calculates a cumulative summation nonparametric extended 
    median test based on the work of Brown & Schaffer (2020) <DOI:10.1080/03610926.2020.1738492>. 
    It then generates a control chart to assess processes and determine if any streams are out of control.
	"""
	
	homepage = "https://github.com/calebgreski/nemtr"
	cran = "nemtr" 

	version("0.0.1.0", md5="cda84a31ed796c1363dbc7a32ea9e0bf")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
