# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShoredate(RPackage):
	"""Shoreline Dating Coastal Stone Age Sites

	Provides tools for shoreline dating coastal Stone Age sites. The 
  implemented method was developed in Roalkvam (2023) 
  <doi:10.1016/j.quascirev.2022.107880> for the Norwegian Skagerrak coast. 
  Although it can be extended to other areas, this also forms the core area for 
  application of the package. Shoreline dating is based on the present-day 
  elevation of a site, a reconstruction of past relative sea-level change, and
  empirically derived estimates of the likely elevation of the sites above the 
  contemporaneous sea-level when they were in use. The geographical and temporal 
  coverage of the method thus follows from the availability of local geological 
  reconstructions of shoreline displacement and the degree to which the 
  settlements to be dated have been located on or close to the shoreline when 
  they were in use. Methods for numerical treatment and visualisation of the 
  dates are provided, along with basic tools for visualising and evaluating the 
  location of sites. 
	"""
	
	homepage = "https://github.com/isakro/shoredate"
	cran = "shoredate" 

	version("1.1.1", md5="0bbd7f39d16b638360fb50eac0f0367b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
