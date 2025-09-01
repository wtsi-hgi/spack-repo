# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsdbHsapiensV99(RPackage):
    """Ensembl based annotation package

    Exposes an annotation databases generated from Ensembl.
    """

    bioc = "EnsDb.Hsapiens.v99"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Hsapiens.v99_2.99.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/EnsDb.Hsapiens.v99/EnsDb.Hsapiens.v99_2.99.0.tar.gz",
    ]

    # Note: Bioconductor may not host this specific EnsDb snapshot. If fetch fails,
    # check the Archive/ listing for the correct package version or nearest available.
    version(
        "2.99.0",
        md5="00000000000000000000000000000000",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/EnsDb.Hsapiens.v99_2.99.0.tar.gz",
    )

    depends_on("r-ensembldb", type=("build", "run"))
