# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXenopuslaeviscdf(RPackage):
    """xenopuslaeviscdf

    A package containing an environment representing the Xenopus_laevis.cdf file.
    """

    bioc = "xenopuslaeviscdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/xenopuslaeviscdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/xenopuslaeviscdf/xenopuslaeviscdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="388ad102c322147c3d394287b0522c8e3968e08d0ff08d095386f777320c9fad",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
