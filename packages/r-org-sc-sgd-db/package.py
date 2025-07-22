# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgScSgdDb(RPackage):
    """Genome wide annotation for Yeast

    Genome wide annotation for Yeast, primarily based on mapping using ORF identifiers from SGD.
    """

    bioc = "org.Sc.sgd.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/org.Sc.sgd.db_3.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/org.Sc.sgd.db/org.Sc.sgd.db_3.18.0.tar.gz",
    ]

    version(
        "3.18.0",
        sha256="595cf311e94a0cddc7e80d83008ac16b47bcefa8453efbbb13f6ca5c2376cf96",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))
