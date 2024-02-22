# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrtester(RPackage):
	"""Likelihood Ratio Tests and Confidence Intervals

	A collection of hypothesis tests and confidence intervals based on the likelihood ratio
    <https://en.wikipedia.org/wiki/Likelihood-ratio_test>.
	"""
	
	cran = "LRTesteR" 

	version("1.1.1", md5="1e79a8ce6752db3465740e0ff408f11f")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
