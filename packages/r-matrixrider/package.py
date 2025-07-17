# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixrider(RPackage):
    """Obtain total affinity and occupancies for binding site matrices on a given sequence

    Calculates a single number for a whole sequence that reflects the propensity of a DNA binding protein to interact with it. The DNA binding protein has to be described with a PFM matrix, for example gotten from Jaspar.
    """

    bioc = "MatrixRider"

    version("1.40.0", commit="e6f4c01153a4e8125d461bd8912f435b0443f9ff")
    version("1.34.0", commit="c7873f6766d2007f223a37df040f7f5552912dec")

    depends_on("r@3.1.2:", type=("build", "run"))
    depends_on("r-tfbstools", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-xvector", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
