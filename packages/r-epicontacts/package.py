# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class REpicontacts(RPackage):
    """A collection of tools for representing epidemiological contact data, composed of case line lists and contacts between cases."""

    homepage = "https://www.repidemicsconsortium.org/epicontacts/"
    cran = "epicontacts"

    version("1.1.3", sha256="c791e60929c412e7e092a7d2c58d5d70675430c9b2db17e6d640328b90a02779")
    version("1.1.2", sha256="2a3e905795fd316253b5027702224ec0696c7e1d3dbce165aef0ed54b1db761f")
    version("1.1.0", sha256="c3013dcc92e3d5790539904add7704168b66b07ecec8e70fef6efc10860f8a38")
    version("1.0.1", sha256="5e8e64684dbd598431d76dd1b729ffd1388341870181a1cdcfad39d7bdcfa8e0")
    version("1.0.0", sha256="4a3b1f413d81e8e25ddbf6bf60aafc41d631cc948941691c525bb6d61a29fd63")

    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-visnetwork", type=("build", "run"))
    depends_on("r-threejs", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-outbreaks", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-covr", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
