# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsar(RPackage):
    """Gene Set Analysis in R

    Gene set analysis using specific alternative hypotheses. Tests for differential expression, scale and net correlation structure.
    """

    bioc = "GSAR"

    version("1.42.0", commit="5d9c73406bdef611b045e5057776e951d12edc8d")
    version("1.36.0", commit="56af0c29e43aeced604e8c6323a2555abb20a281")

    depends_on("r@3.0.1:", type=("build", "run"))
    depends_on("r-igraph@0.7.1:", type=("build", "run"))
