# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYe6100subccdf(RPackage):
    """ye6100subccdf

    A package containing an environment representing the Ye6100subC.CDF file.
    """

    bioc = "ye6100subccdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ye6100subccdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ye6100subccdf/ye6100subccdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="f5c799c0c4a6fd04e8177d7580073418d66dcd72679ec076dcdbbd31da271956",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
