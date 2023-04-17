# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlam(RPackage):
    """Sparse Lightweight Arrays and Matrices.

    Data structures and algorithms for sparse arrays and matrices, based on
    index arrays and simple triplet representations, respectively."""

    cran = "slam"

    version("0.1-50", sha256="7899bf3266c204ecccefc1878f96940b117d4503af128f4fbc50fc409163f8bd")
