# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgug4101aDb(RPackage):
    """Agilent Human 2 cDNA Microarry Kit annotation data (chip hgug4101a)

    Agilent Human 2 cDNA Microarry Kit annotation data (chip hgug4101a) assembled using data from public repositories
    """

    bioc = "hgug4101a.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgug4101a.db_3.2.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgug4101a.db/hgug4101a.db_3.2.3.tar.gz",
    ]

    version(
        "3.2.3",
        sha256="1d6b68f5035e9304e547fe1a63f0ac123480358d51ede97b25bc8a825315dfc2",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))
