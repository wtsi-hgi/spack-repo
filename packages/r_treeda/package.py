# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeda(RPackage):
	"""Tree-Based Discriminant Analysis

	Performs sparse discriminant analysis on a combination of
    node and leaf predictors when the predictor variables are
    structured according to a tree, as described in Fukuyama et
    al. (2017) <doi:10.1371/journal.pcbi.1005706>.
	"""
	
	homepage = "https://github.com/jfukuyama/treeda"
	cran = "treeDA" 

	version("0.0.5", md5="6ce13fdd7681352ba2ff04cdbef871d3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-sparselda@0.1.9:", type=("build", "run"))
	depends_on("r-matrix@1.2.10:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.6:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-gtable@0.2:", type=("build", "run"))
	depends_on("r-phyloseq@1.22.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-ape@5.1:", type=("build", "run"))
