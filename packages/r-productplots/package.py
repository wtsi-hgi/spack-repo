# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProductplots(RPackage):
	"""Product Plots for R

	Framework for visualising tables of counts, proportions
  and probabilities. The framework is called product plots, alluding to
  the computation of area as a product of height and width, and the
  statistical concept of generating a joint distribution from the
  product of conditional and marginal distributions. The framework,
  with extensions, is sufficient to encompass over 20 visualisations
  previously described in fields of statistical graphics and 'infovis',
  including bar charts, mosaic plots, 'treemaps', equal area plots and
  fluctuation diagrams.
	"""
	
	homepage = "https://github.com/hadley/productplots"
	cran = "productplots" 

	version("0.1.1", md5="b2d510473b2bfcba39fa4f05a8b9e664")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
