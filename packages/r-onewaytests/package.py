# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnewaytests(RPackage):
	"""One-Way Tests in Independent Groups Designs

	Performs one-way tests in independent groups designs including homoscedastic and heteroscedastic tests. These are one-way analysis of variance (ANOVA), Welch's heteroscedastic F test, Welch's heteroscedastic F test with trimmed means and Winsorized variances, Brown-Forsythe test, Alexander-Govern test, James second order test, Kruskal-Wallis test, Scott-Smith test, Box F test, Johansen F test, Generalized tests equivalent to Parametric Bootstrap and Fiducial tests, Alvandi's F test, Alvandi's generalized p-value, approximate F test, B square test, Cochran test, Weerahandi's generalized F test, modified Brown-Forsythe test, adjusted Welch's heteroscedastic F test, Welch-Aspin test, Permutation F test. The package performs pairwise comparisons and graphical approaches. Also, the package includes Student's t test, Welch's t test and Mann-Whitney U test for two samples. Moreover, it assesses variance homogeneity and normality of data in each group via tests and plots (Dag et al., 2018, <https://journal.r-project.org/archive/2018/RJ-2018-022/RJ-2018-022.pdf>).
	"""
	
	cran = "onewaytests" 

	version("3.0", md5="3adc7b0e56ef5dc3599c373eb165d9f4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-wesanderson", type=("build", "run"))
