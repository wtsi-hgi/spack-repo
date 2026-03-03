# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLipinskifilters(RPackage):
	"""Computes and Visualize Lipinski's Parameters

	This computes Lipinski Rule of Five parameters and offers visualization for drug discovery. It analyzes molecular properties like molecular weight, hydrogen bond donors, acceptors, and ALogP, providing histograms and pass/fail status plots for efficient compound evaluation, aiding in drug development.
	"""
	
	cran = "LipinskiFilters" 

	version("1.0.1", md5="28f09c22fefd68e5f42f65025c306258")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rcdk@3.8.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-itertools@0.1.3:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
