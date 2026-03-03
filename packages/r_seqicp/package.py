# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqicp(RPackage):
	"""Sequential Invariant Causal Prediction

	Contains an implementation of invariant causal prediction for sequential data. The main function in the package is 'seqICP', which performs linear sequential invariant causal prediction and has guaranteed type I error control. For non-linear dependencies the package also contains a non-linear method 'seqICPnl', which allows to input any regression procedure and performs tests based on a permutation approach that is only approximately correct. In order to test whether an individual set S is invariant the package contains the subroutines 'seqICP.s' and 'seqICPnl.s' corresponding to the respective main methods.
	"""
	
	cran = "seqICP" 

	version("1.1", md5="7bd7fd2b18288d3145cc39eda3c6866d")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-dhsic", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
