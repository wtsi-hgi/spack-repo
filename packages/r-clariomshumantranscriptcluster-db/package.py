# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomshumantranscriptclusterDb(RPackage):
    """Affymetrix clariomshuman annotation data (chip clariomshumantranscriptcluster)

    Affymetrix clariomshuman annotation data (chip clariomshumantranscriptcluster) assembled using data from public repositories
    """

    bioc = "clariomshumantranscriptcluster.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/clariomshumantranscriptcluster.db_8.8.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/clariomshumantranscriptcluster.db/clariomshumantranscriptcluster.db_8.8.0.tar.gz",
    ]

    version(
        "8.8.0",
        sha256="cc1415f897ba1e5e44c7e7cfe4b39eb2be2435e8d5fec6cbf97caf143805cb76",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))
