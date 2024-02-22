# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiplestressr(RPackage):
	"""Additive and Multiplicative Null Models for Multiple Stressor
Data

	An implementation of the additive (Gurevitch et al., 2000 <doi:10.1086/303337>) 
    and multiplicative (Lajeunesse, 2011 <doi:10.1890/11-0423.1>) factorial null models for 
    multiple stressor data (Burgess et al., 2021 <doi:10.1101/2021.07.21.453207>). Effect sizes 
    are able to be calculated for either null model, and subsequently classified into one of 
    four different interaction classifications (e.g., antagonistic or synergistic interactions). 
    Analyses can be conducted on data for single experiments through to large meta-analytical datasets. 
    Minimal input (or statistical knowledge) is required, with any output easily understood. 
    Summary figures are also able to be easily generated.
	"""
	
	homepage = "https://benjburgess.github.io/multiplestressR/"
	cran = "multiplestressR" 

	version("0.1.1", md5="bd32332578c0f4bebf1afe631f5788db")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
