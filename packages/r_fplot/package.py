# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFplot(RPackage):
	"""Automatic Distribution Graphs Using Formulas

	Easy way to plot regular/weighted/conditional distributions by using formulas. The core of the package concerns distribution plots which are automatic: the many options are tailored to the data at hand to offer the nicest and most meaningful graphs possible -- with no/minimum user input. Further provide functions to plot conditional trends and box plots. See <https://lrberge.github.io/fplot/> for more information.
	"""
	
	cran = "fplot" 

	version("1.1.0", md5="5040290ec48649905d7da3bcab978339")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dreamerr@1.1:", type=("build", "run"))
