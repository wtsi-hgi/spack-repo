# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomewidesnp6crlmm(RPackage):
    """Metadata for fast genotyping with the 'crlmm' package

    Package with metadata for fast genotyping Affymetrix GenomeWideSnp_6 arrays using the 'crlmm' package.
    """

    bioc = "genomewidesnp6Crlmm"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/genomewidesnp6Crlmm_1.0.7.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/genomewidesnp6Crlmm/genomewidesnp6Crlmm_1.0.7.tar.gz",
    ]

    version(
        "1.0.7",
        sha256="5d8abdd4ce30ed6695a141f5cb0fc598398fadce0f4cd6ca666d552786ea0c9b",
    )
