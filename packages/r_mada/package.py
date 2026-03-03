# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMada(RPackage):
	"""Meta-Analysis of Diagnostic Accuracy

	Provides functions for diagnostic meta-analysis. Next to basic analysis and visualization the bivariate Model of Reitsma et al. (2005) that is equivalent to the HSROC of Rutter & Gatsonis (2001) can be fitted. A new approach based to diagnostic meta-analysis of Holling et al. (2012) is also available. Standard methods like summary, plot and so on are provided.
	"""
	
	homepage = "r-forge.r-project.org/projects/mada/"
	cran = "mada" 

	version("0.5.11", md5="72316b24a952d41fc554b07e11802a19")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-mvmeta", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
