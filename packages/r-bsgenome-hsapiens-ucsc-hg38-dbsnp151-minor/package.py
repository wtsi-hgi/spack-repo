# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHg38Dbsnp151Minor(RPackage):
    """Full genome sequences for Homo sapiens (UCSC version hg38, based on GRCh38.p12) with injected minor alleles (dbSNP151)

    Full genome sequences for Homo sapiens (Human) as provided by UCSC (hg38, based on GRCh38.p12) with minor alleles injected from dbSNP151, and stored in Biostrings objects. Full genome sequences for Homo sapiens (Human) as provided by UCSC (hg38, based on GRCh38.p12) with minor alleles injected from dbSNP151, and stored in Biostrings objects. Only common single nucleotide variants (SNVs) with at least one alternate allele with frequency greater than 0.01 were considered. For SNVs with more than 1 alternate allele, the most frequent allele was chosen as the minor allele to be injected into the reference genome.
    """

    bioc = "BSgenome.Hsapiens.UCSC.hg38.dbSNP151.minor"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg38.dbSNP151.minor_0.0.9999.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hg38.dbSNP151.minor/BSgenome.Hsapiens.UCSC.hg38.dbSNP151.minor_0.0.9999.tar.gz",
    ]

    version(
        "0.0.9999",
        sha256="23a431e9fc41fa3d6c7d8e23a8fe265c2cb86ea6db7b41522e632a0d27db88f7",
    )

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-bsgenome@1.56:", type=("build", "run"))
