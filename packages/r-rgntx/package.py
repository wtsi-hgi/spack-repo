# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgntx(RPackage):
    """Colocalization analysis of transcriptome elements in the presence of isoform heterogeneity and ambiguity

    RgnTX allows the integration of transcriptome annotations so as to model the complex alternative splicing patterns. It supports the testing of transcriptome elements without clear isoform association, which is often the real scenario due to technical limitations. It involves functions that do permutaion test for evaluating association between features and transcriptome regions.
    """

    bioc = "RgnTX"

    version("1.10.0", commit="682feeb20d2c39e006ecccbd6f21093c77f6f5c4")
    version("1.4.0", commit="0a29f5fc74efac8137fb1ec7ad48fee333541e25")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-regioner", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
