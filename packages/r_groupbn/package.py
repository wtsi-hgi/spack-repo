# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroupbn(RPackage):
	"""Inferring Group Bayesian Networks using Hierarchical Feature
Clustering

	Group Bayesian Networks: This package implements the inference of group Bayesian networks based on hierarchical feature clustering, and the adaptive refinement of the grouping regarding an outcome of interest, as described in Becker et. al (2021) <doi: 10.1371/journal.pcbi.1008735>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "GroupBN" 

	version("1.2.0", md5="68185771d18f170572474932461a7150")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-clustofvar", type=("build", "run"))
	depends_on("r-pcamixdata", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
