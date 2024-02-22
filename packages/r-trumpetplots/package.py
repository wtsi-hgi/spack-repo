# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrumpetplots(RPackage):
	"""Visualization of Genetic Association Studies

	Visualizes the relationship between allele frequency and effect size in genetic association studies. The input is a data frame containing association results. The output is a plot with the effect size of risk variants in the Y axis, and the allele frequency spectrum in the X axis. Corte et al (2023) <doi:10.1101/2023.04.21.23288923>.
	"""
	
	cran = "TrumpetPlots" 

	version("0.0.1.1", md5="2580769e4a1e17c25b3785c5210414a0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
