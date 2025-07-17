# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnplocsHsapiensDbsnp144Grch37(RPackage):
    """SNP locations for Homo sapiens (dbSNP Build 144)

    SNP locations and alleles for Homo sapiens extracted from NCBI dbSNP Build 144. The source data files used for this package were created by NCBI on May 29-30, 2015, and contain SNPs mapped to reference genome GRCh37.p13. WARNING: Note that the GRCh37.p13 genome is a patched version of GRCh37. However the patch doesn't alter chromosomes 1-22, X, Y, MT. GRCh37 itself is the same as the hg19 genome from UCSC *except* for the mitochondrion chromosome. Therefore, the SNPs in this package can be "injected" in BSgenome.Hsapiens.UCSC.hg19 and they will land at the correct position but this injection will exclude chrM (i.e. nothing will be injected in that sequence).
    """

    bioc = "SNPlocs.Hsapiens.dbSNP144.GRCh37"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SNPlocs.Hsapiens.dbSNP144.GRCh37_0.99.20.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/SNPlocs.Hsapiens.dbSNP144.GRCh37/SNPlocs.Hsapiens.dbSNP144.GRCh37_0.99.20.tar.gz",
    ]

    version(
        "0.99.20",
        sha256="3f8e047e5b27a95ae5bc7acbfb4de6aec6c6a65a9edda3eb915b863807e913fd",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SNPlocs.Hsapiens.dbSNP144.GRCh37_0.99.20.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
