# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoe430bcdf(RPackage):
    """moe430bcdf

    A package containing an environment representing the MOE430B.CDF file.
    """

    bioc = "moe430bcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/moe430bcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/moe430bcdf/moe430bcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="6b43c7226d8a7dbecc493eeb10f210a56f51a18558efedc544289c21f1bc857a",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
