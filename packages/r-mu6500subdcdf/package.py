# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu6500subdcdf(RPackage):
    """mu6500subdcdf

    A package containing an environment representing the Mu6500subD.CDF file.
    """

    bioc = "mu6500subdcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu6500subdcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu6500subdcdf/mu6500subdcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="219bed983eef1ac0d2b70d6ff9537b08b6517ecee95393ccdf5145b3e75b0477",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
