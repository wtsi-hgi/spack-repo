# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactomeDb(RPackage):
    """A set of annotation maps for reactome

    A set of annotation maps for reactome assembled using data from reactome. This package has been created by a third-party developer, and is not affiliated with the Reactome team.
    """

    bioc = "reactome.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/reactome.db_1.86.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/reactome.db/reactome.db_1.86.2.tar.gz",
    ]

    version(
        "1.86.2",
        sha256="0c319b4164ab7e590233437ab715dd9a0092287611ac588b74ec42a01b8ce80a",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
