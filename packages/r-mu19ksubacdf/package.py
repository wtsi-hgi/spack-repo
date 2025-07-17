# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu19ksubacdf(RPackage):
    """mu19ksubacdf

    A package containing an environment representing the Mu19KsubA.CDF file.
    """

    bioc = "mu19ksubacdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu19ksubacdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu19ksubacdf/mu19ksubacdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="095c2a372a84ba667d9587db1ed6393a1b140dad4c44964d3d60236bed863630",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
