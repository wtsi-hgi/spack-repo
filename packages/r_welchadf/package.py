# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWelchadf(RPackage):
	"""Welch-James Statistic for Robust Hypothesis Testing under
Heterocedasticity and Non-Normality

	Implementation of Johansen's general formulation of Welch-James's statistic with Approximate Degrees of Freedom, which makes it suitable for testing 
    any linear hypothesis concerning cell means in univariate and multivariate mixed model designs when the data pose non-normality and non-homogeneous variance. Some 
    improvements, namely trimmed means and Winsorized variances, and bootstrapping for calculating an empirical critical value, have been added to the classical formulation. 
    The code departs from a previous SAS implementation by L.M. Lix and H.J. Keselman, available at <http://supp.apa.org/psycarticles/supplemental/met_13_2_110/SAS_Program.pdf> and
    published in Keselman, H.J., Wilcox, R.R., and Lix, L.M. (2003) <DOI:10.1111/1469-8986.00060>.
	"""
	
	homepage = "<http://decsai.ugr.es/~pjvi/r-packages.html>"
	cran = "welchADF" 

	version("0.3.2", md5="ad96f3c71df56fe76f25a7f79b25966b")

	depends_on("r-lme4", type=("build", "run"))
