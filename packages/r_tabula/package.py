# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabula(RPackage):
	"""Analysis and Visualization of Archaeological Count Data

	An easy way to examine archaeological count data. This
    package provides several tests and measures of diversity:
    heterogeneity and evenness (Brillouin, Shannon, Simpson, etc.),
    richness and rarefaction (Chao1, Chao2, ACE, ICE, etc.), turnover and
    similarity (Brainerd-Robinson, etc.). It allows to easily visualize
    count data and statistical thresholds: rank vs abundance plots,
    heatmaps, Ford (1962) and Bertin (1977) diagrams, etc.
	"""
	
	homepage = "https://packages.tesselle.org/tabula/"
	cran = "tabula" 

	version("3.0.1", md5="6b24ceca2667f9bfbd38433c51f731f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arkhe@1.4:", type=("build", "run"))
