# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXtrasnplocsHsapiensDbsnp144Grch38(RPackage):
    """Extra SNP locations for Homo sapiens (dbSNP Build 144)

    Extra SNP locations and alleles for Homo sapiens extracted from NCBI dbSNP Build 144. The source data files used for this package were created by NCBI on May 30, 2015, and contain SNPs mapped to reference genome GRCh38.p2 (a patched version of GRCh38 that doesn't alter chromosomes 1-22, X, Y, MT). While the SNPlocs.Hsapiens.dbSNP144.GRCh38 package contains only molecular variations of class "snp", this package contains molecular variations of other classes (in-del, heterozygous, microsatellite, named-locus, no-variation, mixed, and multinucleotide-polymorphism).
    """

    bioc = "XtraSNPlocs.Hsapiens.dbSNP144.GRCh38"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/XtraSNPlocs.Hsapiens.dbSNP144.GRCh38_0.99.12.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/XtraSNPlocs.Hsapiens.dbSNP144.GRCh38/XtraSNPlocs.Hsapiens.dbSNP144.GRCh38_0.99.12.tar.gz",
    ]

    version(
        "0.99.12",
        sha256="bfa88ea162b41f60a06f5fd7e6364916b4b8637dda00beb911877421a3189834",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/XtraSNPlocs.Hsapiens.dbSNP144.GRCh38_0.99.12.tar.gz",
    )

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
