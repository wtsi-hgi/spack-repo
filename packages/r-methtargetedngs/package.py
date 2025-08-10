# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethtargetedngs(RPackage):
    """Perform Methylation Analysis on Next Generation Sequencing Data

    Perform step by step methylation analysis of Next Generation Sequencing data.
    """

    bioc = "MethTargetedNGS"

    version("1.40.0", commit="6c164a1ae868ca3eed9a88986ed1aea7005dd27e")
    version("1.34.0", commit="b3b59e3c671ef7a9ee132818598f82d59d71b7c4")

    depends_on("r@3.1.2:", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("hmmer@3:", type=("build", "link", "run"))

    def patch(self):
        # Some Bioconductor releases referenced the removed CRAN package
        # 'pwalign'. Replace it with Biostrings which provides the needed
        # pairwise alignment functionality.
        # These edits are tolerant if upstream already removed pwalign.

        # Remove 'pwalign' from DESCRIPTION Depends/Imports lines
        filter_file(
            r"(^\s*(?:Imports|Depends):[\s\S]*?)\bpwalign,?\s*",
            r"\\1",
            "DESCRIPTION",
        )

        # Switch NAMESPACE importFrom(pwalign, ...) -> Biostrings
        filter_file(
            r"importFrom\(pwalign,",
            r"importFrom(Biostrings,",
            "NAMESPACE",
        )

        # Replace explicit namespace qualifiers in R source files
        for r_file in find("R", "*.R"):
            filter_file(r"pwalign::", r"Biostrings::", r_file)

        # Fix malformed DESCRIPTION combining Depends and Imports on one line,
        # which leads R to look for a package literally named 'Imports'.
        filter_file(
            r"^Depends:(.*),\s*Imports:\s*(.*)$",
            r"Depends:\1\nImports: \2",
            "DESCRIPTION",
        )

        # If the previous substitution produced a literal "\\n", convert it to
        # a real newline. Also handle any lingering ", Imports:" occurrences.
        filter_file(r",\s*Imports:\s*", "\nImports: ", "DESCRIPTION")
        filter_file(r"\\nImports:\s*", "\nImports: ", "DESCRIPTION")
