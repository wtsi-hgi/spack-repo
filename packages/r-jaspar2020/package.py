# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaspar2020(RPackage):
    """Data package for JASPAR database (version 2020)

    Data package for JASPAR2020. To search this databases, please use the package TFBSTools (>= 1.23.1).
    """

    homepage = "http://jaspar.genereg.net/"
    bioc = "JASPAR2020"

    version("0.99.8", commit="2299aa5ebe784cd30d37762b1c02303b2720de08")
    version(
        "0.99.10",
        sha256="b9b92d141a317ebb32a14708229f6b82522ceeb5f1b88360d93b0a7cfe30375b",
    )

    depends_on("r@3.6:", type=("build", "run"))
