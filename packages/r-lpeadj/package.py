# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpeadj(RPackage):
	"""A correction of the local pooled error (LPE) method to replace the asymptotic variance adjustment with an unbiased adjustment based on sample size.

	Two options are added to the LPE algorithm. The original LPE method sets all variances below the max variance in the ordered distribution of variances to the maximum variance. in LPEadj this option is turned off by default.  The second option is to use a variance adjustment based on sample size rather than pi/2.  By default the LPEadj uses the sample size based variance adjustment.
	"""
	
	bioc = "LPEadj"

	version("1.62.0", commit="b726227b13daf20d9ea53f0ba62e33cf595216c8")

	depends_on("r-lpe", type=("build", "run"))
