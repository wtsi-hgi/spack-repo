# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseq(RPackage):
    """Bayesian Hierarchical Modeling of ChIP-seq Data Through Hidden Ising Models

    Bayesian hidden Ising models are implemented to identify IP-enriched genomic regions from ChIP-seq data. They can be used to analyze ChIP-seq data with and without controls and replicates.
    """

    bioc = "iSeq"

    version("1.60.0", commit="8f28a55ee4ef712cd62edd3b93e7736459acb41b")
    version("1.54.0", commit="631770a387b50687030a5aa833d9e65d2144d447")

    depends_on("r@2.10:", type=("build", "run"))
