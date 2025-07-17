# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMfascicularisNcbi60(RPackage):
    """Full genome sequences for Macaca fascicularis (Macaca_fascicularis_6.0)

    Full genome sequences for Macaca fascicularis (Crab-eating macaque) as provided by NCBI (assembly Macaca_fascicularis_6.0, assembly accession GCA_011100615.1) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Mfascicularis.NCBI.6.0"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mfascicularis.NCBI.6.0_1.5.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mfascicularis.NCBI.6.0/BSgenome.Mfascicularis.NCBI.6.0_1.5.0.tar.gz",
    ]

    version(
        "1.5.0",
        md5="67272a96950f485d3c0770265f59c85c",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mfascicularis.NCBI.6.0_1.5.0.tar.gz",
    )

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
