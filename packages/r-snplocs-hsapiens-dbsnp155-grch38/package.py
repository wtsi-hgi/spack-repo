# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnplocsHsapiensDbsnp155Grch38(RPackage):
    """Human SNP locations and alleles extracted from dbSNP Build 155 and placed on the GRCh38/hg38 assembly

    The 949,021,448 SNPs in this package were extracted from the RefSNP JSON files for chromosomes 1-22, X, Y, and MT, located at https://ftp.ncbi.nih.gov/snp/archive/b155/JSON/ (these files were created by NCBI in May 2021). These SNPs can be "injected" in BSgenome.Hsapiens.NCBI.GRCh38 or BSgenome.Hsapiens.UCSC.hg38.
    """

    bioc = "SNPlocs.Hsapiens.dbSNP155.GRCh38"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SNPlocs.Hsapiens.dbSNP155.GRCh38_0.99.24.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/SNPlocs.Hsapiens.dbSNP155.GRCh38/SNPlocs.Hsapiens.dbSNP155.GRCh38_0.99.24.tar.gz",
    ]

    version(
        "0.99.24",
        md5="a16b7b1f940c3fcc8fd2d78f438fd25c",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SNPlocs.Hsapiens.dbSNP155.GRCh38_0.99.24.tar.gz",
    )

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
