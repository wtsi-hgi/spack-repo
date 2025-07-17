# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74bcdf(RPackage):
    """mgu74bcdf

    A package containing an environment representing the MG_U74B.cdf file.
    """

    bioc = "mgu74bcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74bcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74bcdf/mgu74bcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="abf46f36f2e2a06bdf1328985564278359a5a940436a74cd3c53d5ac8d7d3b6a",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
