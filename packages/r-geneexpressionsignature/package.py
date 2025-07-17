# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneexpressionsignature(RPackage):
    """Gene Expression Signature based Similarity Metric

    This package gives the implementations of the gene expression signature and its distance to each. Gene expression signature is represented as a list of genes whose expression is correlated with a biological state of interest. And its distance is defined using a nonparametric, rank-based pattern-matching strategy based on the Kolmogorov-Smirnov statistic. Gene expression signature and its distance can be used to detect similarities among the signatures of drugs, diseases, and biological states of interest.
    """

    homepage = "https://github.com/yiluheihei/GeneExpressionSignature"
    bioc = "GeneExpressionSignature"

    version("1.54.0", commit="3281b565a9af5aede5d8ed482abc83ff71ec1913")
    version("1.48.0", commit="7c09f09257a173c1995168da04936b360544b1e8")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
