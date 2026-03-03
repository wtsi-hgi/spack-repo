# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnmtools(RPackage):
	"""Analysis of Niche Evolution using Niche and Distribution Models

	Constructing niche models and analyzing patterns of niche evolution.  Acts as an interface for many popular modeling algorithms, and allows users to conduct Monte Carlo tests to address basic questions in evolutionary ecology and biogeography.  Warren, D.L., R.E. Glor, and M. Turelli (2008) <doi:10.1111/j.1558-5646.2008.00482.x> Glor, R.E., and D.L. Warren (2011) <doi:10.1111/j.1558-5646.2010.01177.x>  Warren, D.L., R.E. Glor, and M. Turelli (2010) <doi:10.1111/j.1600-0587.2009.06142.x> Cardillo, M., and D.L. Warren (2016) <doi:10.1111/geb.12455> D.L. Warren, L.J. Beaumont, R. Dinnage, and J.B. Baumgartner (2019) <doi:10.1111/ecog.03900>.  
	"""
	
	cran = "ENMTools" 

	version("1.1.2", md5="f91704f103be53b85390e3a9d0705cc9")

	depends_on("r-dismo", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-enmeval", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-raster@3.6.3:", type=("build", "run"))
