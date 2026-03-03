# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCogmapr(RPackage):
	"""Cognitive Mapping Tools Based on Coding of Textual Sources

	Functions for building cognitive maps based on qualitative data. Inputs are textual sources (articles, transcription of qualitative interviews of agents,...). These sources have been coded using relations and are linked to (i) a table describing the variables (or concepts) used for the coding and (ii) a table describing the sources (typology of agents, ...). Main outputs are Individual Cognitive Maps (ICM), Social Cognitive Maps (all sources or group of sources) and a list of quotes linked to relations. This package is linked to the work done during the PhD of Frederic M. Vanwindekens (CRA-W / UCL) hold the 13 of May 2014 at University of Louvain in collaboration with the Walloon Agricultural Research Centre (project MIMOSA, MOERMAN fund).
	"""
	
	homepage = "https://frdvnw.gitlab.io/cogmapr/"
	cran = "cogmapr" 

	version("0.9.3", md5="dab687648356e4e5fe6d57c3adc177f5")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
