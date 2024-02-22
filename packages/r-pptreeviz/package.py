# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPptreeviz(RPackage):
	"""Projection Pursuit Classification Tree Visualization

	Tools for exploring projection pursuit classification tree using
    various projection pursuit indexes.
	"""
	
	cran = "PPtreeViz" 

	version("2.0.4", md5="03a14f91dc90f03c3b555bb7b899b182")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
