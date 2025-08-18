# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIeugwasr(RPackage):
    """R Interface to the OpenGWAS Database API.

    R interface to the OpenGWAS database API. Includes a wrapper
    to make generic calls to the API, plus convenience functions for
    specific queries."""

    homepage = "https://github.com/MRCIEU/ieugwasr"
    url = "https://github.com/MRCIEU/ieugwasr/archive/refs/tags/v1.0.0.tar.gz"

    license("MIT")
    version("1.1.0", sha256="2473611654b74abfdcd075a4bfb460657e1c11beef0a0d2943eaff685bb90c57")
    version("1.0.4", sha256="e5e87dc8afff747b2ccabbf439ca01327f65a3273c8e8fac2cdedd67542962e2")
    version("1.0.3", sha256="91d8ba97f5d4953ef1408a3ce317854203ba3d7e07c791765ba825f89531d9c8")
    version("1.0.1", sha256="592d4acedc88f310706fdbe283ef165762d076791e9937d5568cb96ea8f631d6")
    version("1.0.0", sha256="c5c189c6f5c4a7114001dd51d562760de3a6ccade24063685eb4d6348563a31d")
    version("0.2.2", sha256="2530af5e1f8ad54a3eedf9a3a3750099125be79b941f40327ab7f44179d7d8a6")
    version("0.2.1", sha256="e6d8014f1672c6ba019dd03e0b349cc7e5646d76c092b43ebe3ffc0a52e67d33")
    version("0.2.0", sha256="a6462ae142cb331eeede80a47d02ff6d5dfce4bbd10878cd8c7f058fa02508fe")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-googleauthr", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
