# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMfascicularisNcbi50(RPackage):
    """Full genome sequences for Macaca fascicularis (Macaca_fascicularis_5.0)

    Full genome sequences for Macaca fascicularis (long-tailed macaque) as provided by NCBI (Macaca_fascicularis_5.0, 2013-06-12) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Mfascicularis.NCBI.5.0"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mfascicularis.NCBI.5.0_1.4.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mfascicularis.NCBI.5.0/BSgenome.Mfascicularis.NCBI.5.0_1.4.2.tar.gz",
    ]

    version(
        "1.4.2",
        md5="dba6ade39dc6b4f6d06f488141b5550b",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mfascicularis.NCBI.5.0_1.4.2.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
