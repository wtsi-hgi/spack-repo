# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqbias(RPackage):
    """Estimation of per-position bias in high-throughput sequencing data

    This package implements a model of per-position sequencing bias in high-throughput sequencing data using a simple Bayesian network, the structure and parameters of which are trained on a set of aligned reads and a reference genome sequence.
    """

    bioc = "seqbias"

    version("1.50.0", commit="d82941c085ef2bb881595d1ccb8485d7aec7af0b")

    depends_on("r@3.0.2:", type=("build", "run"))
    depends_on("r-genomicranges@0.1:", type=("build", "run"))
    depends_on("r-biostrings@2.15:", type=("build", "run"))
    depends_on("r-rhtslib@1.99.1:", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
    depends_on("curl", type=("build", "link", "run"))
    depends_on("bzip2", type=("build", "link", "run"))
    depends_on("xz", type=("build", "link", "run"))
