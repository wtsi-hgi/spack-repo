# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTernary(RPackage):
	"""Create Ternary and Holdridge Plots

	Plots ternary diagrams (simplex plots / Gibbs triangles) and
  Holdridge life zone plots <doi:10.1126/science.105.2727.367> using the
  standard graphics functions.
  An alternative to 'ggtern', which uses the 'ggplot2' family of plotting 
  functions.
  Includes a 'Shiny' user interface for point-and-click ternary plotting.
	"""
	
	homepage = "https://ms609.github.io/Ternary/"
	cran = "Ternary" 

	version("2.3.1", md5="d42dcc4886855e493e88db7eeff8d1f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpphungarian", type=("build", "run"))
	depends_on("r-plottools@0.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
