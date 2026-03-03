# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatrank(RPackage):
	"""Statistical Rank Aggregation: Inference, Evaluation, and
Visualization

	A set of methods to implement Generalized Method of Moments and Maximal
    Likelihood methods for Random Utility Models. These methods are meant to
    provide inference on rank comparison data. These methods accept full,
    partial, and pairwise rankings, and provides methods to break down full or
    partial rankings into their pairwise components. Please see Generalized
    Method-of-Moments for Rank Aggregation from NIPS 2013 for a description of
    some of our methods.
	"""
	
	cran = "StatRank" 

	version("0.0.6", md5="adc0d1add5c438fe377bab4237f3a201")

	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
