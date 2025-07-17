# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBovinecdf(RPackage):
    """bovinecdf

    A package containing an environment representing the Bovine.cdf file.
    """

    bioc = "bovinecdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/bovinecdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/bovinecdf/bovinecdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="ab9231853e113e3dad7f10cb88935d6979656a2780c2276ca9f3fa06bc07ae8e",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
