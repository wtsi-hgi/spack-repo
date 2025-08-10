# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScanmir(RPackage):
    """scanMiR

    A set of tools for working with miRNA affinity models (KdModels), efficiently scanning for miRNA binding sites, and predicting target repression. It supports scanning using miRNA seeds, full miRNA sequences (enabling 3' alignment) and KdModels, and includes the prediction of slicing and TDMD sites. Finally, it includes utility and plotting functions (e.g. for the visual representation of miRNA-target alignment).
    """

    bioc = "scanMiR"

    version("1.14.0", commit="806c98f0c815a83fd18f256e9cc2b178e35127f6")
    version("1.8.2", commit="6400e75d52957b3ce4c9963bbcf47818f7e7ee9e")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-seqlogo", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-ggseqlogo", type=("build", "link", "run"))

    # Upstream historically imported the removed CRAN package 'pwalign'.
    # We avoid that unavailable dependency by switching references to
    # Biostrings, which provides the required pairwiseAlignment utilities.
    # The edits are tolerant in case upstream already dropped 'pwalign'.
    def patch(self):
        # Remove 'pwalign' from DESCRIPTION Depends/Imports lines (robust)
        # Generic removal anywhere in the file to be safe
        filter_file(r"\bpwalign\b,?\s*", "", "DESCRIPTION")

        # Convert any accidental literal "\n" sequences to real newlines
        filter_file(r"\\n", "\n", "DESCRIPTION")

        # Remove duplicate standalone 'BiocGenerics,' lines to avoid dupes
        filter_file(r"(?m)^\s*BiocGenerics,\s*$\n?", "", "DESCRIPTION")

        # If Imports: is an empty line, seed it with BiocGenerics
        filter_file(r"(?m)^Imports:\s*$", "Imports:\n    BiocGenerics,", "DESCRIPTION")

        # Switch NAMESPACE importFrom(pwalign, ...) -> Biostrings
        filter_file(
            r"importFrom\(pwalign,",
            r"importFrom(Biostrings,",
            "NAMESPACE",
        )

        # Ensure imports for matching helpers are correct with current Bioc:
        # - 'subject' generic lives in IRanges
        # - 'pattern' remains in Biostrings
        filter_file(
            r"importFrom\((?:Biostrings|BiocGenerics),\s*subject\)",
            r"importFrom(IRanges, subject)",
            "NAMESPACE",
        )
        filter_file(
            r"importFrom\(BiocGenerics,\s*pattern\)",
            r"importFrom(Biostrings, pattern)",
            "NAMESPACE",
        )

        # 'type' is not an exported Biostrings symbol; drop such imports
        filter_file(r"^importFrom\(Biostrings,\s*type\)\s*$", "", "NAMESPACE")

        # Replace explicit namespace qualifiers in R source files
        for r_file in find("R", "*.R"):
            filter_file(r"pwalign::", r"Biostrings::", r_file)
