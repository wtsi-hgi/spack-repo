# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocmake(RPackage):
    """CMake for Bioconductor.

    Installs a managed copy of CMake that Bioconductor packages can rely on
    when configuring or building their vendored C/C++ code. Falls back to the
    system CMake if a suitable version is already available."""

    homepage = "https://github.com/LTLA/biocmake"
    urls = [
        "https://www.bioconductor.org/packages/release/bioc/src/contrib/biocmake_1.2.0.tar.gz",
        "https://www.bioconductor.org/packages/3.22/bioc/src/contrib/Archive/biocmake/biocmake_1.2.0.tar.gz",
    ]
    bioc = "biocmake"

    license("MIT")

    version("1.2.0", sha256="cc62588937bf04ed3f3ced2b175d32830c3d16f6f26bcdc6a6dc82d75c5bbdb8")

    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-dir-expiry", type=("build", "run"))

    # Suggests
    depends_on("r-knitr", type=("build"))
    depends_on("r-rmarkdown", type=("build"))
    depends_on("r-biocstyle", type=("build"))
    depends_on("r-testthat", type=("build"))
