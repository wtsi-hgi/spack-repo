# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotbivinvgaus(RPackage):
	"""Density Contour Plot for Bivariate Inverse Gaussian Distribution

	Create the density contour plot for bivariate inverse Gaussian distribution for given non negative random variables.
	"""
	
	cran = "PlotBivInvGaus" 

	version("0.1.0", md5="f159316936aa271f7506a7162173bf72")

	depends_on("r-plotly", type=("build", "run"))
