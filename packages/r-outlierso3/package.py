# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutlierso3(RPackage):
	"""Draws Overview of Outliers (O3) Plots

	Potential outliers are identified for all combinations of a dataset's variables. O3 plots are described in Unwin(2019) <doi:10.1080/10618600.2019.1575226>. The available methods are HDoutliers() from the package 'HDoutliers', FastPCS() from the package 'FastPCS', mvBACON() from 'robustX', adjOutlyingness() from 'robustbase', DectectDeviatingCells() from 'cellWise', covMcd() from 'robustbase'.
	"""
	
	cran = "OutliersO3" 

	version("0.6.3", md5="a19a9a6be1b6cf2d488757c15592d7cb", url="https://cran.r-project.org/src/contrib/OutliersO3_0.6.3.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-hdoutliers", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-robustx", type=("build", "run"))
	depends_on("r-fastpcs", type=("build", "run"))
	depends_on("r-cellwise@2.1:", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-memisc", type=("build", "run"))
