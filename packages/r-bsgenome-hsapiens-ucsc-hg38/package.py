# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHg38(RPackage):
    """Full genomic sequences for Homo sapiens (UCSC genome hg38)

    Full genomic sequences for Homo sapiens as provided by UCSC (genome hg38, based on assembly GRCh38.p14 since 2023/01/31). The sequences are stored in DNAString objects.
    """

    bioc = "BSgenome.Hsapiens.UCSC.hg38"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg38_1.4.5.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hg38/BSgenome.Hsapiens.UCSC.hg38_1.4.5.tar.gz",
    ]

    version(
        "1.4.5",
        md5="b2e670c27944eed77fbe9a9b55be40d2",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg38_1.4.5.tar.gz",
    )
    version(
        "1.4.4",
        md5="360474907caa1c1ed31030f68f80f0a5",
        url="https://bioconductor.org/packages/3.15/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg38_1.4.4.tar.gz",
    )

    depends_on("r@4.2:", type=("build", "run"), when="@1.4.5:")
    depends_on("r-genomeinfodb@1.34.9:", type=("build", "run"))
    depends_on("r-bsgenome@1.66.2:", type=("build", "run"))
