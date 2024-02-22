# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhtboot(RPackage):
	"""Multiple Hypothesis Test Based on Distribution of p Values

	A framework for multiple hypothesis testing based on distribution
    of p values. It is well known that the p values come from different
    distribution for null and alternatives, in this package we provide
    functions to detect that change. We provide a method for using the change
    in distribution of p values as a way to detect the true signals in the
    data.
	"""
	
	cran = "mhtboot" 

	version("1.3.3", md5="51e089df6f962140542d243644b70a44")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
