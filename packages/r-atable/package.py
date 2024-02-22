# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtable(RPackage):
	"""Create Tables for Reporting Clinical Trials

	Create Tables for Reporting Clinical Trials.
  Calculates descriptive statistics and hypothesis tests, 
  arranges the results in a table ready for reporting with LaTeX, HTML or Word.
	"""
	
	homepage = "https://github.com/arminstroebel/atable"
	cran = "atable" 

	version("0.1.14", md5="85747bc0d757f2a2122bac35014f4dee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doby@4.6:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-hmisc@4.1:", type=("build", "run"))
	depends_on("r-settings@0.2.4:", type=("build", "run"))
	depends_on("r-desctools@0.99.24:", type=("build", "run"))
	depends_on("r-effsize@0.7.1:", type=("build", "run"))
