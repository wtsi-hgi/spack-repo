# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylscaper(RPackage):
    """Visualization of Methylation Data

    methylscaper is an R package for processing and visualizing data jointly profiling methylation and chromatin accessibility (MAPit, NOMe-seq, scNMT-seq, nanoNOMe, etc.). The package supports both single-cell and single-molecule data, and a common interface for jointly visualizing both data types through the generation of ordered representational methylation-state matrices. The Shiny app allows for an interactive seriation process of refinement and re-weighting that optimally orders the cells or DNA molecules to discover methylation patterns and nucleosome positioning.
    """

    bioc = "methylscaper"

    version("1.16.0", commit="2bc3c44d1fff414fc31f3544a71f6ba9ffc641ef")
    version("1.10.0", commit="e2d8ace362666efa39a7efc0ba8bd0ba05b5af60")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-seriation", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-rfast", type=("build", "run"))
    depends_on("r-shinyfiles", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r@4.4.0:", when="@1.16.0:", type=("build", "run"))

    def patch(self):
        # Drop 'pwalign' from DESCRIPTION Imports to avoid removed CRAN dep
        filter_file(r"^\s*pwalign,\s*\n", "", "DESCRIPTION")

        # Ensure BiocGenerics is listed in Imports (needed for 'score' generic)
        filter_file(
            r"^(\s*Biostrings,\s*\n)",
            "\\1  BiocGenerics,\n",
            "DESCRIPTION",
        )

        # Switch NAMESPACE imports from pwalign -> Biostrings for alignment helpers
        filter_file(r"importFrom\(pwalign,", r"importFrom(Biostrings,", "NAMESPACE")
        # But import 'score' from BiocGenerics, not Biostrings
        filter_file(
            r"importFrom\(Biostrings,\s*score\)",
            r"importFrom(BiocGenerics, score)",
            "NAMESPACE",
        )
