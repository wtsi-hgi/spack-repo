# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanine2cdf(RPackage):
    """canine2cdf

    A package containing an environment representing the Canine_2.cdf file.
    """

    bioc = "canine2cdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/canine2cdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/canine2cdf/canine2cdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="196bb3704e01f85634c92d953a3964a6bf59f0707886fa65df6036096dadec1c",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
