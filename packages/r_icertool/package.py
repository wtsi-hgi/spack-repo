# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcertool(RPackage):
	"""Calculate and Plot ICER

	The app will calculate the ICER (incremental cost-effectiveness 
             ratio) Rawlins (2012) <doi:10.1016/B978-0-7020-4084-9.00044-6> from the mean 
             costs and quality-adjusted life years (QALY) Torrance and Feeny (2009) <doi:10.1017/S0266462300008461>
             for a set of treatment options, and draw the efficiency frontier 
             in the costs-effectiveness plane. The app automatically identifies 
             and excludes dominated and extended-dominated options from the ICER 
             calculation.
	"""
	
	cran = "icertool" 

	version("0.0.3", md5="85b30c31a490ade4ec449c62bfb52749")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-shinyhelper", type=("build", "run"))
