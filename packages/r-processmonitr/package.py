# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcessmonitr(RPackage):
	"""Building Process Monitoring Dashboards

	Functions for constructing dashboards for business process monitoring. Building on the event log objects class from package 'bupaR'. Allows the use to assemble custom shiny dashboards based on process data.
	"""
	
	homepage = "https://www.bupar.net"
	cran = "processmonitR" 

	version("0.1.0", md5="6b12ace91e1c12f1e1bddc73cea66252")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-bupar", type=("build", "run"))
	depends_on("r-edear", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
