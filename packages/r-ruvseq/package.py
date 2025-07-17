# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuvseq(RPackage):
    """Remove Unwanted Variation from RNA-Seq Data

    This package implements the remove unwanted variation (RUV) methods of Risso et al. (2014) for the normalization of RNA-Seq read counts between samples.
    """

    homepage = "https://github.com/drisso/RUVSeq"
    bioc = "RUVSeq"

    version("1.42.0", commit="d6cbf4506d72a421e4f64d6da74cf8dc3d9e94b7")
    version("1.36.0", commit="09a26da683406dacb1d56486ed41cf62e4378c32")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-edaseq@1.99.1:", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
