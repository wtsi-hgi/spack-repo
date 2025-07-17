# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPqsfinder(RPackage):
    """Identification of potential quadruplex forming sequences

    Pqsfinder detects DNA and RNA sequence patterns that are likely to fold into an intramolecular G-quadruplex (G4). Unlike many other approaches, pqsfinder is able to detect G4s folded from imperfect G-runs containing bulges or mismatches or G4s having long loops. Pqsfinder also assigns an integer score to each hit that was fitted on G4 sequencing data and corresponds to expected stability of the folded G4.
    """

    homepage = "https://pqsfinder.fi.muni.cz"
    bioc = "pqsfinder"

    version("2.24.0", commit="0ee51f582b3f2dd903a7d7d75110c48799233b7a")
    version("2.18.0", commit="3f8caa0d963e03b17d1a6d6001b00253e1b1b2b2")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-bh@1.78:", type=("build", "run"))
