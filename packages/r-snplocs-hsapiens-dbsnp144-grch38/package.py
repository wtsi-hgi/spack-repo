# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnplocsHsapiensDbsnp144Grch38(RPackage):
    """SNP locations for Homo sapiens (dbSNP Build 144)

    SNP locations and alleles for Homo sapiens extracted from NCBI dbSNP Build 144. The source data files used for this package were created by NCBI on May 30, 2015, and contain SNPs mapped to reference genome GRCh38.p2 (a patched version of GRCh38 that doesn't alter chromosomes 1-22, X, Y, MT). Note that these SNPs can be "injected" in BSgenome.Hsapiens.NCBI.GRCh38 or in BSgenome.Hsapiens.UCSC.hg38.
    """

    bioc = "SNPlocs.Hsapiens.dbSNP144.GRCh38"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SNPlocs.Hsapiens.dbSNP144.GRCh38_0.99.20.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/SNPlocs.Hsapiens.dbSNP144.GRCh38/SNPlocs.Hsapiens.dbSNP144.GRCh38_0.99.20.tar.gz",
    ]

    version(
        "0.99.20",
        sha256="b6c6ae8d3a866501146e325d40dc1695b26b522c6f9d063218fc6466bbd5b57b",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SNPlocs.Hsapiens.dbSNP144.GRCh38_0.99.20.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
