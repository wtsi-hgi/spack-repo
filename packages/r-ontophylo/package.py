# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROntophylo(RPackage):
	"""Ontology-Informed Phylogenetic Comparative Analyses

	Provides new tools for analyzing discrete trait data integrating bio-ontologies and phylogenetics. It expands on the previous work of Tarasov et al. (2019) <doi:10.1093/isd/ixz009>. The PARAMO pipeline allows to reconstruct ancestral phenomes treating groups of morphological traits as a single complex character. The pipeline incorporates knowledge from ontologies during the amalgamation of individual character stochastic maps.
  Here we expand the current PARAMO functionality by adding new statistical methods for inferring evolutionary phenome dynamics using non-homogeneous Poisson process (NHPP). The new functionalities include: (1) reconstruction of evolutionary rate shifts of phenomes across lineages and time; (2) reconstruction of morphospace dynamics through time; and (3) estimation of rates of phenome evolution at different levels of anatomical hierarchy (e.g., entire body or specific regions only). The package also includes user-friendly tools for visualizing evolutionary rates of different anatomical regions using vector images of the organisms of interest.
	"""
	
	homepage = "https://github.com/diegosasso/ontophylo"
	cran = "ontophylo" 

	version("1.1.3", md5="7d4ccd471a3e6218f7a481cf24f20e97")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-fancova", type=("build", "run"))
	depends_on("r-grimport", type=("build", "run"))
