# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgdoe(RPackage):
	"""Modern Graphs for Design of Experiments with 'ggplot2'

	Generate commonly used plots in the field of design of experiments using 'ggplot2'.
  'ggDoE' currently supports the following plots: alias matrix, box cox transformation, boxplots, lambda plot,
  regression diagnostic plots, half normal plots, main and interaction effect plots for factorial designs,
  contour plots for response surface methodology, Pareto plot, and two dimensional projections of a latin hypercube design.
	"""
	
	homepage = "https://ggdoe.netlify.app"
	cran = "ggDoE" 

	version("0.8", md5="0c75e49d9f259c7f43495bc7d98163ee")

	depends_on("r@3.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-insight@0.19.5:", type=("build", "run"))
