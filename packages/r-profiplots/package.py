# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfiplots(RPackage):
	"""Profinit Plotting Theme

	Help unify visual output of R analyses in the Profinit EU company. 
  So far, there are color and fill scales for 'ggplot2', plotting theme for 
  'ggplot2', color palettes and utils to make the tools default choices.
	"""
	
	homepage = "https://profinit.eu"
	cran = "profiplots" 

	version("0.2.3", md5="967844291c3258f9bfa9eaf483d48969")

	depends_on("r-ggplot2@3.2:", type=("build", "run"))
