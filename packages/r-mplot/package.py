# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMplot(RPackage):
	"""Graphical Model Stability and Variable Selection Procedures

	Model stability and variable inclusion plots [Mueller and Welsh
    (2010, <doi:10.1111/j.1751-5823.2010.00108.x>); Murray, Heritier and Mueller
    (2013, <doi:10.1002/sim.5855>)] as well as the adaptive fence [Jiang et al.
    (2008, <doi:10.1214/07-AOS517>); Jiang et al. 
    (2009, <doi:10.1016/j.spl.2008.10.014>)] for linear and generalised linear models.
	"""
	
	homepage = "https://garthtarr.github.io/mplot/"
	cran = "mplot" 

	version("1.0.6", md5="78087394e1789662440a3a99a036c03c")

	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-bestglm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-googlevis", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
