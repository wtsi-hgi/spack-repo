# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSklarsomega(RPackage):
	"""Measuring Agreement Using Sklar's Omega Coefficient

	Provides tools for applying Sklar's Omega (Hughes, 2018) <arXiv:1803.02734>
    methodology to nominal scores, ordinal scores, percentages, counts, amounts (i.e.,
    non-negative real numbers), and balances (i.e., any real number). The framework can
    accommodate any number of units, any number of coders, and missingness; and
    can be used to measure agreement with a gold standard, intra-coder agreement,
    and/or inter-coder agreement. Frequentist inference is supported for all levels
    of measurement. Bayesian inference is supported for continuous scores only.
	"""
	
	cran = "sklarsomega" 

	version("3.0-2", md5="6378b6df1cccb3a17f24cbbf0fb22058")

	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mcmcse", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
