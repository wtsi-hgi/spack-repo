# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabup(RPackage):
	"""Bayesian Meta-Analysis Using Basic Uncertain Pooling

	Contains functions that allow Bayesian meta-analysis (1) with binomial data, counts(y) and total counts (n) or, (2) with user-supplied point estimates and associated variances.   Case (1) provides an analysis based on the logit transformation of the sample proportion. This methodology is also appropriate for combining data from sample surveys and related sources. The functions can  calculate the corresponding similarity matrix. More details can be found in Cahoy and Sedransk (2023), Cahoy and Sedransk (2022)  <doi:10.1007/s42519-018-0027-2>, Evans and Sedransk (2001) <doi:10.1093/biomet/88.3.643>, and Malec and Sedransk (1992) <doi:10.1093/biomet/79.3.593>.
	"""
	
	cran = "metabup" 

	version("0.1.3", md5="7b5c36e68e923329cacd9e6b99dc2f0d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
