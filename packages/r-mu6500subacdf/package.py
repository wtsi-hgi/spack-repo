# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu6500subacdf(RPackage):
    """mu6500subacdf

    A package containing an environment representing the Mu6500subA.CDF file.
    """

    bioc = "mu6500subacdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu6500subacdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu6500subacdf/mu6500subacdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="c9769a4af339cd3145805dc2e72ab2f7a35409f1afa8ab9a3183fdff64e8c797",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
