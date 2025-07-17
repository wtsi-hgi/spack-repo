# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpivizrserver(RPackage):
    """WebSocket server infrastructure for epivizr apps and packages

    This package provides objects to manage WebSocket connections to epiviz apps. Other epivizr package use this infrastructure.
    """

    homepage = "https://epiviz.github.io"
    bioc = "epivizrServer"

    version("1.36.0", commit="b74c0989b2f9606b9e33d246d710858df3746305")
    version("1.30.0", commit="c71d56a1985605545f922ef828f5ef57a88e8387")

    depends_on("r@3.2.3:", type=("build", "run"))
    depends_on("r-httpuv@1.3:", type=("build", "run"))
    depends_on("r-r6@2:", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-mime@0.2:", type=("build", "run"))
