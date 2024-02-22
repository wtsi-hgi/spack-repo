# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVistree(RPackage):
	"""Visualization of Subgroups for Decision Trees

	Provides a visualization for characterizing subgroups defined by a decision tree structure. The visualization simplifies the ability to interpret individual pathways to subgroups; each sub-plot describes the distribution of observations within individual terminal nodes and percentile ranges for the associated inner nodes.
	"""
	
	cran = "visTree" 

	version("0.8.1", md5="07051af972ca7bcf5bff1a56a0218aa7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
