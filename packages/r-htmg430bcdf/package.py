# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430bcdf(RPackage):
    """htmg430bcdf

    A package containing an environment representing the HT_MG-430B.cdf file.
    """

    bioc = "htmg430bcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htmg430bcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htmg430bcdf/htmg430bcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="f027e045b6e0b45cf9f2f0be67477c01433ee08a76900eb06f68e9433e2819a8",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
