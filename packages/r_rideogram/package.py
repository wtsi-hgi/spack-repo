# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRideogram(RPackage):
	"""Drawing SVG Graphics to Visualize and Map Genome-Wide Data on
Idiograms

	For whole-genome analysis, idiograms are virtually the most intuitive and effective way to map and visualize the genome-wide information. RIdeogram was developed to visualize and map whole-genome data on idiograms with no restriction of species.
	"""
	
	cran = "RIdeogram" 

	version("0.2.2", md5="d7d7a3a24d020eec2a9e108210821ab9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-grimport2", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
