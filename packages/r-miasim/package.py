# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiasim(RPackage):
    """Microbiome Data Simulation

    Microbiome time series simulation with generalized Lotka-Volterra model, Self-Organized Instability (SOI), and other models. Hubbell's Neutral model is used to determine the abundance matrix. The resulting abundance matrix is applied to (Tree)SummarizedExperiment objects.
    """

    homepage = "https://github.com/microbiome/miaSim"
    bioc = "miaSim"

    version("1.14.0", commit="da3162c98749800d9af48bc0f0e95491bed4dfe6")
    version("1.8.0", commit="0e9233948402688b100e982b0e56b64e59b89fa8")

    depends_on("r-treesummarizedexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-desolve", type=("build", "run"))
    depends_on("r-powerlaw", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
