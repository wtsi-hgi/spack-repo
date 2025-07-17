# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXlaevisDb(RPackage):
    """Affymetrix Xenopus laevis annotation data (chip xlaevis)

    Affymetrix Xenopus laevis annotation data (chip xlaevis) assembled using data from public repositories
    """

    bioc = "xlaevis.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/xlaevis.db_3.2.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/xlaevis.db/xlaevis.db_3.2.3.tar.gz",
    ]

    version(
        "3.2.3",
        sha256="a3b474f621a54f08362cdc9e4f1bf88687125de58075e789458bba8b5838b131",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-xl-eg-db@3.3:", type=("build", "run"))
