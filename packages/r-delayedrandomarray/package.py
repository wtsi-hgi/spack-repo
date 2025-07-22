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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DelayedRandomArray_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DelayedRandomArray/DelayedRandomArray_1.10.0.tar.gz"]

	version("1.10.0", sha256="df2c9d8d3acec7813e052755104e1d6c7e38f27f3d0728737f1f224f28314453")

	depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
