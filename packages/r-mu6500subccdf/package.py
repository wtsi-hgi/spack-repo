# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu6500subccdf(RPackage):
    """mu6500subccdf

    A package containing an environment representing the Mu6500subC.CDF file.
    """

    bioc = "mu6500subccdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu6500subccdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu6500subccdf/mu6500subccdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="013434805957d6d53f235b9b4aab684ec9f2937c016139cbcb5a9f7959e1d4dd",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
