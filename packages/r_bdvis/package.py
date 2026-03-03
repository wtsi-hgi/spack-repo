# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdvis(RPackage):
	"""Biodiversity Data Visualizations

	Provides a set of functions to create basic visualizations to quickly
    preview different aspects of biodiversity information such as inventory 
    completeness, extent of coverage (taxonomic, temporal and geographic), gaps
    and biases. Barve & Otegui (2016) <DOI:10.1093/bioinformatics/btw333>.
	"""
	
	cran = "bdvis" 

	version("0.2.37", md5="de5be0c17a4ac39fc0771c194854940a")

	depends_on("r-maps", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
	depends_on("r-treemap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
