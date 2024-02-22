# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancertiming(RPackage):
	"""Estimation of Temporal Ordering of Cancer Abnormalities

	Timing copy number changes using estimates of mutational allele frequency from resequencing of tumor samples.
	"""
	
	cran = "cancerTiming" 

	version("3.1.8", md5="c795c58b82dab306fe0f12afea076107")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-learnbayes", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
