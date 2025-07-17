# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtratfocuscdf(RPackage):
    """htratfocuscdf

    A package containing an environment representing the HT_Rat-Focus.cdf file.
    """

    bioc = "htratfocuscdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htratfocuscdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htratfocuscdf/htratfocuscdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="a93be8803cb24fb1cd1387ab374ad1f27979f9f74bb748d163c24a7d823f164b",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
