# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcheofrag(RPackage):
	"""Refitting and Spatial Analysis in Archaeology

	Methods to analyse fragmented objects in archaeology using refitting relationships between fragments scattered in archaeological spatial units (e.g. stratigraphic layers). Graphs and graph theory are used to model archaeological observations. The package is mainly based on the 'igraph' package for graph analysis. Functions can: 1) create, manipulate, and simulate fragmentation graphs, 2) measure the cohesion and admixture of archaeological spatial units, and 3) characterise the topology of a specific set of refitting relationships. An empirical dataset is also provided as an example. Documentation about 'archeofrag' is provided by the vignette included in this package and by the accompanying scientific papers: Plutniak (2021, Journal of Archaeological Science, <doi:10.1016/j.jas.2021.105501>) and Plutniak (2022, Journal of Open Source Software, <doi:10.21105/joss.04335>).
	"""
	
	homepage = "https://github.com/sebastien-plutniak/archeofrag"
	cran = "archeofrag" 

	version("0.8.2", md5="648092ba796ae46ecea0eb6d5088a64b")

	depends_on("r-igraph", type=("build", "run"))
