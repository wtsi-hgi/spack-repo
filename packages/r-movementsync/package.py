# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMovementsync(RPackage):
	"""Analysis and Visualisation of Musical Audio and Video Movement
Synchrony Data

	Analysis and visualisation of synchrony, interaction, and joint
    movements from audio and video movement data of a group of music performers. The demo is data described in Clayton, Leante, and 
    Tarsitani (2021) <doi:10.17605/OSF.IO/KS325>, while example analyses 
    can be found in Clayton, Jakubowski, and Eerola (2019) 
    <doi:10.1177/1029864919844809>. Additionally, wavelet analysis 
    techniques have been applied to examine movement-related 
    musical interactions, as shown in Eerola et al. (2018)
    <doi:10.1098/rsos.171520>.
	"""
	
	cran = "movementsync" 

	version("0.1.4", md5="1a210f370cc73a83f220a4c4ed9481df")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-osfr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-waveletcomp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
