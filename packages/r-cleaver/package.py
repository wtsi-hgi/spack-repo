# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleaver(RPackage):
    """Cleavage of Polypeptide Sequences

    In-silico cleavage of polypeptide sequences. The cleavage rules are taken from: http://web.expasy.org/peptide_cutter/peptidecutter_enzymes.html
    """

    homepage = "https://github.com/sgibb/cleaver/"
    bioc = "cleaver"

    version("1.46.0", commit="cea8ee3779600f3bc9546cdebed61966e98a2876")
    version("1.40.0", commit="180eed41e3aa4abcc18ee542ba153e4ba195604e")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-biostrings@1.29.8:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
