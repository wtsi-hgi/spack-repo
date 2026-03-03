# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTernMmrm(RPackage):
	"""Tables and Graphs for Mixed Models for Repeated Measures (MMRM)

	Mixed models for repeated measures (MMRM) are a popular choice for 
  analyzing longitudinal continuous outcomes in randomized clinical trials and beyond;
  see for example Cnaan, Laird and Slasor (1997) 
  <doi:10.1002/(SICI)1097-0258(19971030)16:20%3C2349::AID-SIM667%3E3.0.CO;2-E>.
  This package provides an interface for fitting MMRM within the 
  'tern' <https://cran.r-project.org/package=tern> framework by Zhu et al. (2023)
  and tabulate results easily using 'rtables' <https://cran.r-project.org/package=rtables>
  by Becker et al. (2023). It builds on 'mmrm' <https://cran.r-project.org/package=mmrm> 
  by Sabanés Bové et al. (2023) for the actual MMRM computations.
	"""
	
	homepage = "https://github.com/insightsengineering/tern.mmrm"
	cran = "tern.mmrm" 

	version("0.3.0", md5="3b37a0f99591369e0233cc960349dff5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tern@0.9.3:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-emmeans@1.6:", type=("build", "run"))
	depends_on("r-formatters@0.5.5:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mmrm@0.3.5:", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rtables@0.6.6:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
