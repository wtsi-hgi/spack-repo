# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRacmacs(RPackage):
	"""Antigenic Cartography Macros

	A toolkit for making antigenic maps from immunological assay data,
    in order to quantify and visualize antigenic differences between different
    pathogen strains as described in
    Smith et al. (2004) <doi:10.1126/science.1097211> and used in the World
    Health Organization influenza vaccine strain selection process. Additional
    functions allow for the diagnostic evaluation of antigenic maps and an
    interactive viewer is provided to explore antigenic relationships amongst
    several strains and incorporate the visualization of associated genetic
    information.
	"""
	
	homepage = "https://acorg.github.io/Racmacs/"
	cran = "Racmacs" 

	version("1.2.9", md5="0c413b16808ef3cfd980abd22bc3de05")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-brotli", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rmarchingcubes", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppensmallen", type=("build", "run"))
	depends_on("r-rapidjsonr", type=("build", "run"))
