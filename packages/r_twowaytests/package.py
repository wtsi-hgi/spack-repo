# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwowaytests(RPackage):
	"""Two-Way Tests in Independent Groups Designs

	Performs two-way tests in independent groups designs. These are two-way ANOVA, two-way ANOVA under heteroscedasticity: parametric bootstrap based generalized test and generalized pivotal quantity based generalized test (Ananda et al., 2022) <doi:10.1080/03610926.2022.2059682>, two-way ANOVA for medians, trimmed means, M-estimators (Wilcox, 2011; ISBN:978-0-12-386983-8). The package performs descriptive statistics and graphical approaches. Moreover, it assesses variance homogeneity and normality of data in each group via tests and plots. All 'twowaytests' functions are designed for two-way layout.
	"""
	
	cran = "twowaytests" 

	version("1.3", md5="a8730596906972d7880b3637507cb23e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-onewaytests", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-wesanderson", type=("build", "run"))
