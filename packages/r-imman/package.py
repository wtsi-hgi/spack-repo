# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImman(RPackage):
    """Interlog protein network reconstruction by Mapping and Mining ANalysis

    Reconstructing Interlog Protein Network (IPN) integrated from several Protein protein Interaction Networks (PPINs). Using this package, overlaying different PPINs to mine conserved common networks between diverse species will be applicable.
    """

    bioc = "IMMAN"

    version("1.28.0", commit="64beff68a13f145c2c1b232fc44dfa752ef06d57")
    version("1.22.0", commit="561195579065e60624167f72f60f235b3bd06b55")

    depends_on("r-stringdb", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-seqinr", type=("build", "run"))

    def patch(self):
        # Some Bioconductor releases of IMMAN list the removed CRAN package
        # 'pwalign' in DESCRIPTION/NAMESPACE. Since IMMAN only needs
        # Biostrings::pairwiseAlignment, we drop the pwalign requirement and
        # redirect imports/usages to Biostrings.
        # - Tolerate absence of these entries if upstream already fixed them.

        # Remove 'pwalign' from DESCRIPTION Depends/Imports lines
        filter_file(
            r"(^\s*(?:Imports|Depends):[\s\S]*?)\bpwalign,?\s*",
            r"\1",
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
