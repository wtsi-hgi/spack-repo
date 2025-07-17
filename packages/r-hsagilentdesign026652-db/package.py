# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsagilentdesign026652Db(RPackage):
    """Agilent Chips that use Agilent design number 026652 annotation data (chip HsAgilentDesign026652)

    Agilent Chips that use Agilent design number 026652 annotation data (chip HsAgilentDesign026652) assembled using data from public repositories
    """

    bioc = "HsAgilentDesign026652.db"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/HsAgilentDesign026652.db_3.2.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/HsAgilentDesign026652.db/HsAgilentDesign026652.db_3.2.3.tar.gz",
    ]

    version(
        "3.2.3",
        sha256="7d1776b0364fc5f46ba887cdb1c0bb7d72858a17433181c6c5642256ffeed674",
    )

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))
