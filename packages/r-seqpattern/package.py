# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqpattern(RPackage):
    """Visualising oligonucleotide patterns and motif occurrences across a set of sorted sequences

    Visualising oligonucleotide patterns and sequence motifs occurrences across a large set of sequences centred at a common reference point and sorted by a user defined feature.
    """

    bioc = "seqPattern"

    version("1.40.0", commit="ed8c9708fad3427d0a899234341a3111b41c673a")
    version("1.34.0", commit="0441ed0424d43c666274eecf5256c5ace816a15b")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-kernsmooth", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
