# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredictioninterval(RPackage):
	"""Prediction Interval Functions for Assessing Replication Study
Results

	A common problem faced by journal reviewers and authors is the question of
     whether the results of a replication study are consistent with the original
     published study. One solution to this problem is to examine the effect size
     from the original study and generate the range of effect sizes that could
     reasonably be obtained (due to random sampling) in a replication attempt
     (i.e., calculate a prediction interval). This package has functions that calculate
     the prediction interval for the correlation (i.e., r),
     standardized mean difference (i.e., d-value), and mean.
	"""
	
	cran = "predictionInterval" 

	version("1.0.0", md5="24ca1d8d7e6e1d8e8ec628b1d0cc651f")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
