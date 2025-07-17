# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepsnv(RPackage):
    """Detection of subclonal SNVs in deep sequencing data.

    This package provides provides quantitative variant callers for detecting subclonal mutations in ultra-deep (>=100x coverage) sequencing experiments. The deepSNV algorithm is used for a comparative setup with a control experiment of the same loci and uses a beta-binomial model and a likelihood ratio test to discriminate sequencing errors and subclonal SNVs. The shearwater algorithm computes a Bayes classifier based on a beta-binomial model for variant calling with multiple samples for precisely estimating model parameters - such as local error rates and dispersion - and prior knowledge, e.g. from variation data bases such as COSMIC.
    """

    bioc = "deepSNV"

    version("1.54.0", commit="0c0cbd6c8b5f7486a56a1286bed2a221719c3bca")
    version("1.48.0", commit="38615a9352e9985a47e59527630fc05103558630")

    depends_on("r@2.13:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-vgam", type=("build", "run"))
    depends_on("r-variantannotation@1.27.6:", type=("build", "run"))
    depends_on("r-rhtslib@1.13.1:", type=("build", "run"))
