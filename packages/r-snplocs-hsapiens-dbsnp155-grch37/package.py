# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnplocsHsapiensDbsnp155Grch37(RPackage):
    """Human SNP locations and alleles extracted from dbSNP Build 155 and placed on the GRCh37/hg19 assembly

    The 929,496,192 SNPs in this package were extracted from the RefSNP JSON files for chromosomes 1-22, X, Y, and MT, located at https://ftp.ncbi.nih.gov/snp/archive/b155/JSON/ (these files were created by NCBI in May 2021). These SNPs can be "injected" in BSgenome.Hsapiens.UCSC.hg19.
    """

    bioc = "SNPlocs.Hsapiens.dbSNP155.GRCh37"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SNPlocs.Hsapiens.dbSNP155.GRCh37_0.99.24.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/SNPlocs.Hsapiens.dbSNP155.GRCh37/SNPlocs.Hsapiens.dbSNP155.GRCh37_0.99.24.tar.gz",
    ]

    version(
        "0.99.24",
        md5="9473e23ffc7ae76e630a78324b245da8",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SNPlocs.Hsapiens.dbSNP155.GRCh37_0.99.24.tar.gz",
    )

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
