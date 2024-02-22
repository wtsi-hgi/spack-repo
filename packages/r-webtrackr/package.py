# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebtrackr(RPackage):
	"""Preprocessing and Analyzing Web Tracking Data

	Data structures and methods to work with web tracking data. The functions cover data preprocessing steps, enriching web tracking data with external information and methods for the analysis of digital behavior as used in several academic papers (e.g., Clemm von Hohenberg et al., 2023 <doi:10.17605/OSF.IO/M3U9P>; Stier et al., 2022 <doi:10.1017/S0003055421001222>).
	"""
	
	homepage = "https://github.com/schochastics/webtrackR"
	cran = "webtrackR" 

	version("0.1.0", md5="d912dcf5e915e292b04dad02ba9835a5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
