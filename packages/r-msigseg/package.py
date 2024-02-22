# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsigseg(RPackage):
	"""Multiple SIGnal SEGmentation

	Traditional methods typically detect breakpoints from individual signals, which means that when applied separately to multiple signals, the breakpoints are not aligned. 
    However, this package implements a common breakpoint detection approach for multiple piecewise constant signals, resulting in increased detection sensitivity and specificity. 
    By employing various techniques, optimal performance is ensured, and computation is accelerated. We hope that this package will be beneficial for researchers in signal processing, bioinformatics, economy, and other related fields.
    The segmentation(), lambda_estimator() functions are the main functions of this package.
	"""
	
	cran = "MSigSeg" 

	version("0.2.0", md5="4593b0044fcfdd194722bf4ae9d6d1be")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
