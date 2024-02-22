# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHilldiv(RPackage):
	"""Integral Analysis of Diversity Based on Hill Numbers

	Tools for analysing, comparing, visualising and partitioning diversity based on Hill numbers.
  'hilldiv' is an R package that provides a set of functions to assist analysis of diversity for
  diet reconstruction, microbial community profiling or more general ecosystem characterisation
  analyses based on Hill numbers, using OTU/ASV tables and associated phylogenetic trees as
  inputs. The package includes functions for (phylo)diversity measurement, (phylo)diversity
  profile plotting, (phylo)diversity comparison between samples and groups, (phylo)diversity
  partitioning and (dis)similarity measurement. All of these grounded in abundance-based and
  incidence-based Hill numbers.
  The statistical framework developed around Hill numbers encompasses many of the most
  broadly employed diversity (e.g. richness, Shannon index, Simpson index),
  phylogenetic diversity (e.g. Faith's PD, Allen's H, Rao's quadratic entropy) and
  dissimilarity (e.g. Sorensen index, Unifrac distances) metrics. This enables the most
  common analyses of diversity to be performed while grounded in a single statistical
  framework. The methods are described in Jost et al. (2007) <DOI:10.1890/06-1736.1>,
  Chao et al. (2010) <DOI:10.1098/rstb.2010.0272> and Chiu et al. (2014)
  <DOI:10.1890/12-0960.1>; and reviewed in the framework of molecularly characterised
  biological systems in Alberdi & Gilbert (2019) <DOI:10.1111/1755-0998.13014>.
	"""
	
	homepage = "https://github.com/anttonalberdi/hilldiv"
	cran = "hilldiv" 

	version("1.5.1", md5="66c580a798624e2ff1ff2aad934c6298")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-fsa", type=("build", "run"))
