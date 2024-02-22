# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelayedrandomarray(RPackage):
	"""Delayed Arrays of Random Values

	Implements a DelayedArray of random values where the realization of the sampled values is delayed until they are needed. Reproducible sampling within any subarray is achieved by chunking where each chunk is initialized with a different random seed and stream. The usual distributions in the stats package are supported, along with scalar, vector and arrays for the parameters.
	"""
	
	homepage = "https://github.com/LTLA/DelayedRandomArray"
	bioc = "DelayedRandomArray" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DelayedRandomArray_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DelayedRandomArray/DelayedRandomArray_1.10.0.tar.gz"]

	version("1.10.0", md5="2f583ab177fd333cf626827fc28a6faf")

	depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
