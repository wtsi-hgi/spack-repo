# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisstatistics(RPackage):
	"""Automated Visualization of Statistical Tests

	Visualization of the most powerful statistical hypothesis test.
    The function vistat() visualizes the statistical hypothesis testing between the 
    dependent variable (response) varsample and the independent variable (feature) varfactor. 
    The statistical hypothesis test (including the eventual corresponding post-hoc analysis) with
    the highest statistical power fulfilling the assumptions of the corresponding test is chosen based on a decision tree.
    A graph displaying the raw data accordingly to the chosen test is generated, the test statistics including eventual 
    post-hoc-analysis are returned. The automated workflow is especially suited for browser based interfaces to 
    server-based deployments of R. Implemented tests: lm(), t.test(), wilcox.test(), aov(), kruskal.test(), fisher.test(), chisqu.test().
    Implemented tests to check the normal distribution of standardized residuals: shapiro.test() and ad.test().
    Implemented post-hoc tests: TukeyHSD() for aov() and pairwise.wilcox.test() for kruskal.test().
    For the comparison of averages, the following algorithm is implemented: 
    If the p-values of the standardized residuals of both shapiro.test() or ad.test() are smaller 
    than 1-conf.level, kruskal.test() resp. wilcox.test() are performed, otherwise the oneway.test()
    and aov() resp. t.test() are performed and displayed. Exception: 
    If the sample size is bigger than 100, t.test() is always performed and wilcox.test() is never executed 
    (Lumley et al. (2002) <doi:10.1146/annurev.publhealth.23.100901.140546>).
    For the test of independence of count data, Cochran's rule (Cochran (1954) <doi:10.2307/3001666>) is implemented: 
    If more than 20 percent of all cells have a count smaller than 5, fisher.test() is performed and displayed,
    otherwise chisqu.test(). In both cases case an additional mosaic plot is generated. 
	"""
	
	cran = "visStatistics" 

	version("0.1.1", md5="1f5d65f0ee4cf47341bdf626e669eab5")

	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
