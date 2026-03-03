# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscoursegt(RPackage):
	"""Analyze Group Patterns using Graph Theory in Educational
Settings

	Analyzes group patterns using discourse analysis data with
    graph theory mathematics. Takes the order of which individuals talk
    and converts it to a network edge and weight list. Returns the
    density, centrality, centralization, and subgroup information for each
    group. Based on the analytical framework laid out in Chai et al.
    (2019) <doi:10.1187/cbe.18-11-0222>.
	"""
	
	cran = "discourseGT" 

	version("1.2.0", md5="2a25b0fcdcf501ceaa58dc64341b69b0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
