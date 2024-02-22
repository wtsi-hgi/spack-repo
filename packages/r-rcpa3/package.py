# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpa3(RPackage):
	"""Data and Functions for R Companion to Political Analysis 3rd Ed

	Bundles the datasets and functions featured in Philip H. 
    Pollock and Barry C. Edwards<https://edge.sagepub.com/pollock>, "An R Companion to Political Analysis, 3rd Edition," Thousand Oaks, CA: Sage Publications.
	"""
	
	cran = "RCPA3" 

	version("1.2.1", md5="b9f3e13a8f9f386c7aa1b9334f1abd45", url="https://cran.r-project.org/src/contrib/RCPA3_1.2.1.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-descr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
