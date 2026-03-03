# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoliscidata(RPackage):
	"""Datasets and Functions Featured in Pollock and Edwards, an R
Companion to Essentials of Political Analysis, Second Edition

	Bundles the datasets and functions used in the textbook by Philip
    Pollock and Barry Edwards, an R Companion to Essentials of Political Analysis,
    Second Edition.
	"""
	
	cran = "poliscidata" 

	version("2.3.0", md5="82e68759fe6d13c315817a6d19e60a6d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-descr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
