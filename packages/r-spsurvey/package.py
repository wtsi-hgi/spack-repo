# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpsurvey(RPackage):
	"""Spatial Sampling Design and Analysis

	A design-based approach to statistical inference, with a focus on spatial data. Spatially balanced samples are selected using the Generalized Random Tessellation Stratified (GRTS) algorithm. The GRTS algorithm can be applied to finite resources (point geometries) and infinite resources (linear / linestring and areal / polygon geometries) and flexibly accommodates a diverse set of sampling design features, including stratification, unequal inclusion probabilities, proportional (to size) inclusion probabilities, legacy (historical) sites, a minimum distance between sites, and two options for replacement sites (reverse hierarchical order and nearest neighbor). Data are analyzed using a wide range of analysis functions that perform categorical variable analysis, continuous variable analysis, attributable risk analysis, risk difference analysis, relative risk analysis, change analysis, and trend analysis. spsurvey can also be used to summarize objects, visualize objects, select samples that are not spatially balanced, select panel samples, measure the amount of spatial balance in a sample, adjust design weights, and more. For additional details, see Dumelle et al. (2023) <doi:10.18637/jss.v105.i03>.
	"""
	
	homepage = "https://usepa.github.io/spsurvey/"
	cran = "spsurvey" 

	version("5.5.1", md5="626e886690d366c01170d4c41ab090e3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-survey@4.1.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-crossdes", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
