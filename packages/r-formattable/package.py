# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormattable(RPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://renkun-ken.github.io/formattable/"
    cran = "formattable"

    version("0.2.1", sha256="4f0d4d2267d87a42da777066dd992c44fcc8ba9c0bdd2cbfc72980573b88bded")
    version("0.2.0.1", sha256="2e935699fb8c68f55cad824ee2ff76acdb6ee0f363a4342a6f9b0809ea93f2e8")
    version("0.2", sha256="1deac133feb9498b08d002a8e2db311d7d1937f4f506fcbe7575f8280ef9a52c")
    version("0.1.5", sha256="4b6173d4861ec7f86aa1d88c071be548253b698b32edb58258a00922ffb5034e")

    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
