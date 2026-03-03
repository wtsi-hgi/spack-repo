# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViscomp(RPackage):
	"""Visualize Multi-Component Interventions in Network Meta-Analysis

	A set of functions providing several visualization tools for exploring the behavior of the components in a network meta-analysis of multi-component (complex) interventions: 
   - components descriptive analysis
   - heat plot of the two-by-two component combinations 
   - leaving one component combination out scatter plot 
   - violin plot for specific component combinations' effects
   - density plot for components' effects  
   - waterfall plot for the interventions' effects that differ by a certain component combination 
   - network graph of components
   - rank heat plot of components for multiple outcomes.
   The implemented tools are described by Seitidis et al. (2023) <doi:10.1002/jrsm.1617>.
	"""
	
	homepage = "https://github.com/georgiosseitidis/viscomp"
	cran = "viscomp" 

	version("1.0.0", md5="53ed6f35c89d385380970a92122acc4d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-circlize@0.4.15:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-ggextra@0.10:", type=("build", "run"))
	depends_on("r-ggnewscale@0.4.8:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-hmisc@4.7:", type=("build", "run"))
	depends_on("r-mass@7.3.56:", type=("build", "run"))
	depends_on("r-netmeta@1.3.0:", type=("build", "run"))
	depends_on("r-plyr@1.8.7:", type=("build", "run"))
	depends_on("r-qgraph@1.9.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
