# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRigraphlib(RPackage):
    """igraph library as an R package.

    Vendors the igraph C sources and builds them as a static library that
    other Bioconductor packages can link against without shipping their own
    igraph copy."""

    homepage = "https://github.com/libscran/Rigraphlib"
    urls = [
        "https://www.bioconductor.org/packages/release/bioc/src/contrib/Rigraphlib_1.2.0.tar.gz",
        "https://www.bioconductor.org/packages/3.22/bioc/src/contrib/Archive/Rigraphlib/Rigraphlib_1.2.0.tar.gz",
    ]
    bioc = "Rigraphlib"

    license("GPL-3")

    version("1.2.0", sha256="a4291fb8e03b16f08130ca74fc9e0d00b9bd90196b48c084202324cfe51310a4")

    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-biocmake", type=("build", "run"))
    depends_on("cmake@3.24:", type="build")

    # Suggests
    depends_on("r-knitr", type=("build"))
    depends_on("r-rmarkdown", type=("build"))
    depends_on("r-biocstyle", type=("build"))
    depends_on("r-testthat", type=("build"))
