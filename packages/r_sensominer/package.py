# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensominer(RPackage):
	"""Sensory Data Analysis

	Statistical Methods to Analyse Sensory Data. SensoMineR: A package for sensory data analysis. S. Le and F. Husson (2008).
	"""
	
	homepage = "http://sensominer.free.fr"
	cran = "SensoMineR" 

	version("1.27", md5="14aa1393d06a1838a54271adbeec656a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-factominer@2.7:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-algdesign", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
