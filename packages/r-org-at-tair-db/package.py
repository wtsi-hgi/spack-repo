# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgAtTairDb(RPackage):
    """Genome wide annotation for Arabidopsis

    Genome wide annotation for Arabidopsis, primarily based on mapping using TAIR identifiers.
    """

    bioc = "org.At.tair.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.At.tair.db_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.At.tair.db/org.At.tair.db_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="81baae5188e3c0a184e662437e905126bd9a9ddc1c7f6b972caed87bbd83998e",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
