# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoe430acdf(RPackage):
    """moe430acdf

    A package containing an environment representing the MOE430A.CDF file.
    """

    bioc = "moe430acdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/moe430acdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/moe430acdf/moe430acdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="e0b48097f682f7fc493254d3b827adc325e8813b342bf35db5c870a6b2608d58",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
