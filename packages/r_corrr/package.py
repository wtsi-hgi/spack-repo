# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrr(RPackage):
	"""Correlations in R

	A tool for exploring correlations.  It makes it possible to
    easily perform routine tasks when exploring correlation matrices such
    as ignoring the diagonal, focusing on the correlations of certain
    variables against others, or rearranging and visualizing the matrix in
    terms of the strength of the correlations.
	"""
	
	homepage = "https://github.com/tidymodels/corrr"
	cran = "corrr" 

	version("0.4.4", md5="7c20f515294247b388566bbd85e861a8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-ggrepel@0.6.5:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-seriation@1.2.0:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
