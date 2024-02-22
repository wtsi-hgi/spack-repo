# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdiver(RPackage):
	"""Visualization of Viral Protein Sequence Diversity Dynamics

	To ease the visualization of outputs from Diversity Motif Analyser ('DiMA';
    <https://github.com/BVU-BILSAB/DiMA>). 'vDiveR' allows visualization of the diversity 
    motifs (index and its variants – major, minor and unique) for elucidation of 
    the underlying inherent dynamics. Please refer <https://vdiver-manual.readthedocs.io/en/latest/>
    for more information.
	"""
	
	cran = "vDiveR" 

	version("1.2.1", md5="d8cad43e07002940adf2d8e94463ec4a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gghalves", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
