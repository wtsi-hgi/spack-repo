# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimlandr(RPackage):
	"""Simulation-Based Landscape Construction for Dynamical Systems

	A toolbox for constructing potential landscapes for dynamical
    systems using Monte Carlo simulation.  The method is based on the
    potential landscape definition by Wang et al. (2008)
    <doi:10.1073/pnas.0800579105> (also see Zhou & Li, 2016
    <doi:10.1063/1.4943096> for further mathematical discussions) and can
    be used for a large variety of models.
	"""
	
	homepage = "https://sciurus365.github.io/simlandr/"
	cran = "simlandr" 

	version("0.3.1", md5="8df648fcc027ea8b67976ff0ba187cb8")

	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
