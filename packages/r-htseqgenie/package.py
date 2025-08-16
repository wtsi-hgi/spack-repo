# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtseqgenie(RPackage):
    """A NGS analysis pipeline.

    Libraries to perform NGS analysis.
    """

    bioc = "HTSeqGenie"

    version("4.38.0", commit="1638d9f96a469fbe25232d1f2ab8c869f6b7ddb1")
    version("4.32.0", commit="9a84f3dd4f2e12b916b09292c59ecec8fa78715b")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-gmapr@1.8:", type=("build", "run"))
    depends_on("r-shortread@1.19.13:", type=("build", "run"))
    depends_on("r-variantannotation@1.8.3:", type=("build", "run"))
    depends_on("r-biocgenerics@0.2:", type=("build", "run"))
    depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
    depends_on("r-iranges@1.21.39:", type=("build", "run"))
    depends_on("r-genomicranges@1.23.21:", type=("build", "run"))
    depends_on("r-rsamtools@1.8.5:", type=("build", "run"))
    depends_on("r-biostrings@2.24.1:", type=("build", "run"))
    depends_on("r-chipseq@1.6.1:", type=("build", "run"))
    depends_on("r-hwriter@1.3:", type=("build", "run"))
    depends_on("r-cairo@1.5.5:", type=("build", "run"))
    depends_on("r-genomicfeatures@1.9.31:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-rtracklayer@1.17.19:", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-varianttools@1.7.7:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    # Missing runtime dependency discovered during R CMD INSTALL
    depends_on("r-pwalign", type=("build", "run"))
