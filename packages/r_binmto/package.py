# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinmto(RPackage):
	"""Many-to-One Comparisons of Proportions

	Asymptotic simultaneous confidence intervals for comparison of many treatments with one control,
 for the difference of binomial proportions, allows for Dunnett-like-adjustment, Bonferroni or unadjusted intervals.
 Simulation of power of the above interval methods, approximate calculation of any-pair-power, and sample size
 iteration based on approximate any-pair power. Exact conditional maximum test for many-to-one comparisons to a control.
	"""
	
	cran = "binMto" 

	version("0.0-7", md5="7ddafb7540e86f996223a53be426c6fa")

	depends_on("r-mvtnorm", type=("build", "run"))
