# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsa2dist(RPackage):
    """MSA2dist calculates pairwise distances between all sequences of a DNAStringSet or a AAStringSet using a custom score matrix and conducts codon based analysis

    MSA2dist calculates pairwise distances between all sequences of a DNAStringSet or a AAStringSet using a custom score matrix and conducts codon based analysis. It uses scoring matrices to be used in these pairwise distance calcualtions which can be adapted to any scoring for DNA or AA characters. E.g. by using literal distances MSA2dist calculates pairwise IUPAC distances.
    """

    homepage = "https://gitlab.gwdg.de/mpievolbio-it/MSA2dist"
    bioc = "MSA2dist"

    version("1.12.0", commit="d7a8634defc569af6557bb350e6e392b42f8d161")
    version("1.6.0", commit="c88df72118c7639191c8be67515187bfde898d5f")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-rcppthread", type=("build", "run"))
    depends_on("r@4.4.0:", when="@1.12.0:", type=("build", "run"))

    def patch(self):
        # Some releases reference the removed CRAN package 'pwalign'.
        # Drop that dependency and redirect any imports/usages to Biostrings,
        # which provides pairwiseAlignment and related helpers.
        # These edits are tolerant if upstream already removed pwalign.

        # Remove 'pwalign' from DESCRIPTION Depends/Imports lines
        filter_file(
            r"(^\s*(?:Imports|Depends):[\s\S]*?)\bpwalign,?\s*",
            r"\1",
            "DESCRIPTION",
        )
        # Fallback: in case the DESCRIPTION formatting is unusual, do a
        # conservative token drop anywhere in the file for 'pwalign'
        filter_file(r"\bpwalign,?\s*", "", "DESCRIPTION")

        # Switch NAMESPACE importFrom(pwalign, ...) -> Biostrings
        filter_file(
            r"importFrom\(pwalign,",
            r"importFrom(Biostrings,",
            "NAMESPACE",
        )

        # Replace explicit namespace qualifiers in R source files
        for r_file in find("R", "*.R"):
            filter_file(r"pwalign::", r"Biostrings::", r_file)

        # Redirect internal helper acquisition from pwalign -> Biostrings
        # makePostalignedSeqs is a thin alias to an internal helper; prefer Biostrings
        # Replace the dynamic getter with a lightweight implementation that
        # wraps the PairwiseAlignments object into an AAStringSet
        filter_file(
            r"^makePostalignedSeqs\s*<-\s*get\('\.makePostalignedSeqs',\s*$",
            (
                "makePostalignedSeqs <- function(x) {\n"
                "    patt <- as.character(Biostrings::pattern(x))\n"
                "    subj <- as.character(Biostrings::subject(x))\n"
                "    return(list(Biostrings::AAStringSet(c(patt, subj))))\n"
                "}\n"
            ),
            join_path("R", "makePostalignedSeqs.R"),
        )
        # Drop the now-stale continuation line
        filter_file(r"envir=asNamespace\('pwalign'\), inherits=FALSE\)", "", join_path("R", "makePostalignedSeqs.R"))

        # Load substitution matrices from Biostrings instead of pwalign
        filter_file(
            r"package=\"pwalign\"",
            r"package=\"Biostrings\"",
            join_path("R", "aa2selfscore.R"),
        )
        # Fix any accidental backslash-escaped quotes introduced by regexes
        filter_file(r"\\\"Biostrings\\\"", r'"Biostrings"', join_path("R", "aa2selfscore.R"))
