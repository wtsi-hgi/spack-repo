# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebrafishcdf(RPackage):
    """zebrafishcdf

    A package containing an environment representing the Zebrafish.cdf file.
    """

    bioc = "zebrafishcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/zebrafishcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/zebrafishcdf/zebrafishcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="a0671d41dffb074d19d808bf6d4e7972c8d65fa21ec3a5a2da342eba20ee016b",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
