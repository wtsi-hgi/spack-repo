# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlizer(RPackage):
    """Comprehensive QTL annotation of GWAS results

    This R package provides access to the Qtlizer web server. Qtlizer annotates lists of common small variants (mainly SNPs) and genes in humans with associated changes in gene expression using the most comprehensive database of published quantitative trait loci (QTLs).
    """

    bioc = "Qtlizer"

    version("1.22.0", commit="736158f0360206c03ef8b06d82c47f41a52ffe71")
    version("1.16.0", commit="89c3ba564a369281652cc8e0e28b00183a521601")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
