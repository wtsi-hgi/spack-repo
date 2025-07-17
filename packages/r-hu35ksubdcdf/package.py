# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubdcdf(RPackage):
    """hu35ksubdcdf

    A package containing an environment representing the Hu35KsubD.CDF file.
    """

    bioc = "hu35ksubdcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubdcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubdcdf/hu35ksubdcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="5b081f10d0efd1792fb67c874b670aa85566a4d62b119021a7cdae109fab41f3",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
