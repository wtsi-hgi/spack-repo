# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasillatranscriptexpr(RPackage):
    """Data package with transcript expression obtained with kallisto from pasilla knock-down RNA-Seq data from Brooks et al.

    Provides kallisto workflow and transcript expression of RNA-Seq data from Brooks et al.
    """

    bioc = "PasillaTranscriptExpr"

    version("1.36.0", commit="a074b672661e032a09ec5b59d05b6a8b2ca98eef")
    version("1.30.0", commit="7260020be3e0e6e3bc414e36a23559abb7404eca")

    depends_on("r@3.3:", type=("build", "run"))
