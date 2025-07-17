# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrain(RPackage):
    """Baffling Recursive Algorithm for Isotope distributioN calculations

    Package for calculating aggregated isotopic distribution and exact center-masses for chemical substances (in this version composed of C, H, N, O and S). This is an implementation of the BRAIN algorithm described in the paper by J. Claesen, P. Dittwald, T. Burzykowski and D. Valkenborg.
    """

    bioc = "BRAIN"

    version("1.54.0", commit="e7bf6b8e2bd9f2d73f1f02c7cbe63fdd78eb6c04")
    version("1.48.0", commit="735542d1c3f917a2287373bb653bb5df5c1974a9")

    depends_on("r@2.8.1:", type=("build", "run"))
    depends_on("r-polynomf", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
