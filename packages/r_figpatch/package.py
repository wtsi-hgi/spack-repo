# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFigpatch(RPackage):
	"""Easily Arrange External Figures with Patchwork Alongside
'ggplot2' Figures

	For including external figures into an assembled 
    {patchwork}. This enables the creation of more complex figures that include 
    images alongside plots. 
	"""
	
	homepage = "https://github.com/BradyAJohnston/figpatch"
	cran = "figpatch" 

	version("0.2", md5="5078cfeb83e61b08ae53b4a830f3a022")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
