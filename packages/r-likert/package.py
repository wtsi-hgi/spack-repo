# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLikert(RPackage):
	"""Analysis and Visualization Likert Items

	An approach to analyzing Likert response items, with an emphasis on visualizations. 
    The stacked bar plot is the preferred method for presenting Likert results. Tabular results
    are also implemented along with density plots to assist researchers in determining whether 
    Likert responses can be used quantitatively instead of qualitatively. See the likert(), 
    summary.likert(), and plot.likert() functions to get started.
	"""
	
	homepage = "http://jason.bryer.org/likert"
	cran = "likert" 

	version("1.3.5", md5="fb07254b02aebb936c979902d01326f5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
