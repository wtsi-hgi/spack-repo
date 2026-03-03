# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRotatogram(RPackage):
	"""A Non-Axis-Dominant Association Plotting Tool

	A rotatogram is a method of displaying an association which is axis non-dominant. This is achieved in two ways: First, the method of estimating the slope and intercept uses the least-products method rather than more typical least squared error for the "dependent" variable. The least products method has no "dependent" variable and is scale independent. Second, the plot is rotated such that the resulting regression line is vertical, reducing the suggestion that the vertical axis is the dominant one. The slope can be read relative to either axis equally.
	"""
	
	cran = "rotatogram" 

	version("0.1.3", md5="4511afdaee92122844cd380eea3fa307")

	depends_on("r-ggplot2", type=("build", "run"))
