# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeleganscdf(RPackage):
    """celeganscdf

    A package containing an environment representing the Celegans.CDF file.
    """

    bioc = "celeganscdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/celeganscdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/celeganscdf/celeganscdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="f7743bafe91f4047ed4a28ea3778726e4cd6ad3b0bab218388e07d858802dc28",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
