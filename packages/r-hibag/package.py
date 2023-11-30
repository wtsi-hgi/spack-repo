# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHibag(RPackage):
    """Imputes HLA classical alleles using GWAS SNP data, and it relies on a training set of HLA and SNP genotypes. HIBAG can be used by researchers with published parameter estimates instead of requiring access to large training sample datasets. It combines the concepts of attribute bagging, an ensemble classifier method, with haplotype inference for SNPs and HLA types. Attribute bagging is a technique which improves the accuracy and stability of classifier ensembles using bootstrap aggregating and random variable selection."""

    homepage = "https://bioconductor.org/packages/release/bioc/html/HIBAG.html"
    url = "https://bioconductor.org/packages/release/bioc/src/contrib/HIBAG_1.38.0.tar.gz"
    bioc = "HIBAG"

    version("1.38.0", sha256="fc40338194a290248af4170a8fd1080babddf668e0a692365b4a9e0cbc2b8561")

    depends_on("r-rcppparallel", type=("build", "run"))
