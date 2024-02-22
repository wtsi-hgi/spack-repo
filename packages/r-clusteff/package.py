# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusteff(RPackage):
	"""Clusters of Effects Curves in Quantile Regression Models

	Clustering method to cluster both effects curves, through quantile regression coefficient modeling, and curves in functional data analysis. Sottile G. and Adelfio G. (2019) <doi:10.1007/s00180-018-0817-8>.
	"""
	
	cran = "clustEff" 

	version("0.3.1", md5="6d7582fe01186a057a3fd7ff5764c262")

	depends_on("r-qrcm", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
