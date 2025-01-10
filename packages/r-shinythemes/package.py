# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinythemes(RPackage):
    """Themes for Shiny"""

    homepage = "https://rstudio.github.io/shinythemes/"
    cran = "shinythemes"

    maintainers("dorton21")

    version("1.2.0", sha256="37d68569ce838c7da9f0ea7e2b162ecf38fba2ae448a4888b6dd29c4bb5b2963")

    depends_on("r@3.0.0:", type=("build", "run"))
    depends_on("r-shiny@0.11:", type=("build", "run"))
