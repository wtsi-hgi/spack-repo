# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgquiver(RPackage):
	"""Quiver Plots for 'ggplot2'

	An extension of 'ggplot2' to provide quiver plots to visualise vector fields. 
    This functionality is implemented using a geom to produce a new graphical layer, which
    allows aesthetic options. This layer can be overlaid on a map to improve visualisation
    of mapped data.
	"""
	
	homepage = "https://github.com/mitchelloharawild/ggquiver"
	cran = "ggquiver" 

	version("0.3.3", md5="d25ca6c8aa4a705b92eab619499d8a97")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
