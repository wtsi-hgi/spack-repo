# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenextender(RPackage):
    """Optimized Functional Annotation Of ChIP-seq Data

    geneXtendeR optimizes the functional annotation of ChIP-seq peaks by exploring relative differences in annotating ChIP-seq peak sets to variable-length gene bodies.  In contrast to prior techniques, geneXtendeR considers peak annotations beyond just the closest gene, allowing users to see peak summary statistics for the first-closest gene, second-closest gene, ..., n-closest gene whilst ranking the output according to biologically relevant events and iteratively comparing the fidelity of peak-to-gene overlap across a user-defined range of upstream and downstream extensions on the original boundaries of each gene's coordinates.  Since different ChIP-seq peak callers produce different differentially enriched peaks with a large variance in peak length distribution and total peak count, annotating peak lists with their nearest genes can often be a noisy process.  As such, the goal of geneXtendeR is to robustly link differentially enriched peaks with their respective genes, thereby aiding experimental follow-up and validation in designing primers for a set of prospective gene candidates during qPCR.
    """

    homepage = "https://github.com/Bohdan-Khomtchouk/geneXtendeR"
    bioc = "geneXtendeR"

    version("1.34.0", commit="3c384e5462c30381c26775d5ec0ec1787904e6b0")
    version("1.28.0", commit="c8e88150a7a2a2c0125b7dd07f0df7ab6c4daea5")

    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-networkd3", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-snowballc", type=("build", "run"))
    depends_on("r-tm", type=("build", "run"))
    depends_on("r-wordcloud", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-org-rn-eg-db", type=("build", "run"))
