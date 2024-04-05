# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlatetools(RPackage):
	"""Tools and Plots for Multi-Well Plates

	Collection of functions for working with multi-well microtitre
    plates, mainly 96, 384 and 1536 well plates.
	"""
	
	homepage = "https://github.com/swarchal/platetools"
	cran = "platetools" 

	version("0.1.7", md5="8ac37c9a8d360af1911b363dc2d0c702")
	version("0.1.5", md5="874323a58d80ea8dacc6149859800caa")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
