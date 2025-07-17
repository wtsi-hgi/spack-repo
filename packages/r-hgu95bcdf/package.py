# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95bcdf(RPackage):
    """hgu95bcdf

    A package containing an environment representing the HG_U95B.CDF file.
    """

    bioc = "hgu95bcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95bcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95bcdf/hgu95bcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="927a33d1a0735be868a0fea70231f6d687c479554051620889b194002ee83682",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
