# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCottoncdf(RPackage):
    """cottoncdf

    A package containing an environment representing the Cotton.cdf file.
    """

    bioc = "cottoncdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/cottoncdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/cottoncdf/cottoncdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="e5fa3f2ed7a3e9ec7961f3b0ac532118c186b2ba3fbee95bebcb059214e5dc75",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
