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

    version("1.16.0", commit="7030e8b5ac6fb6a7ca2e23f08faae25f3b2a1559")
    version("1.10.0", commit="828b10a93a01b9c21294db19b35211659910fa83")

    depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
    depends_on("r-dqrng", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
