# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBacon(RPackage):
    """Controlling bias and inflation in association studies using the empirical null distribution

    Bacon can be used to remove inflation and bias often observed in epigenome- and transcriptome-wide association studies. To this end bacon constructs an empirical null distribution using a Gibbs Sampling algorithm by fitting a three-component normal mixture on z-scores.
    """

    bioc = "bacon"

    version("1.36.0", commit="9c7068639a9734c716100e05e93e455fe94a5d12")
    version("1.30.0", commit="90f4e323f894a58c693af8c810eee65a622d4593")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-ellipse", type=("build", "run"))
