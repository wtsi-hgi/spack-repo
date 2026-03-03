# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanalysis(RPackage):
	"""Benchmarking and Rescaling R2 using Noise Percentile Analysis

	Provides the tools needed to benchmark the R2 value corresponding to a certain acceptable noise level while also providing a rescaling function based on that noise level yielding a new value of R2 we refer to as R2k which is independent of both the number of degrees of freedom and the noise distribution function.
	"""
	
	cran = "pAnalysis" 

	version("2.0", md5="0da15d9a1ed0db9e270e6d1484ab31a3")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
