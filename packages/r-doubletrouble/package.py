# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoubletrouble(RPackage):
    """Identification and classification of duplicated genes

    doubletrouble aims to identify duplicated genes from whole-genome protein sequences and classify them based on their modes of duplication. The duplication modes are i. segmental duplication (SD); ii. tandem duplication (TD); iii. proximal duplication (PD); iv. transposed duplication (TRD) and; v. dispersed duplication (DD). Transposon-derived duplicates (TRD) can be further subdivided into rTRD (retrotransposon-derived duplication) and dTRD (DNA transposon-derived duplication). If users want a simpler classification scheme, duplicates can also be classified into SD- and SSD-derived (small-scale duplication) gene pairs. Besides classifying gene pairs, users can also classify genes, so that each gene is assigned a unique mode of duplication. Users can also calculate substitution rates per substitution site (i.e., Ka and Ks) from duplicate pairs, find peaks in Ks distributions with Gaussian Mixture Models (GMMs), and classify gene pairs into age groups based on Ks peaks.
    """

    homepage = "https://github.com/almeidasilvaf/doubletrouble"
    bioc = "doubletrouble"

    version("1.8.0", commit="524ccf4e279bfa00a304f22be59ec673b56bd214")
    version("1.2.5", commit="4004e47f036d8962dbf7df1dec6c8dcdbe8957b2")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-syntenet", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-msa2dist@1.1.5:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
