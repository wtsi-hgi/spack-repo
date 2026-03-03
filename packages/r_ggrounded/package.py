# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgrounded(RPackage):
	"""Rounded Bar Plots

	Creates bar plots with rounded corners using 'ggplot2'.
    The code in this package was adapted from a solution provided by 
    Stack Overflow user 'sthoch' in the following post
    <https://stackoverflow.com/questions/62176038/r-ggplot2-bar-chart-with-round-corners-on-top-of-bar>.
	"""
	
	homepage = "https://github.com/botan/ggrounded"
	cran = "ggrounded" 

	version("0.0.3", md5="9bb6d3bfc1edb427168df3f899f4602a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridgeometry", type=("build", "run"))
