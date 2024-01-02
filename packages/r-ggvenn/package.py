# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgvenn(RPackage):
    """An easy-to-use way to draw pretty venn diagram by 'ggplot2'."""

    cran = "ggvenn"

    version("0.1.10", sha256="cde116f117266cca27d8cd20205512e602c23514db6d97caaa950b9b21fa873e")
    version("0.1.9", sha256="38779cfa4e01e07d4a42453cfb8b93d32d2acd6187676bae7d11b2168714a52e")
    version("0.1.8", sha256="35be03ebe6e15e6b0d16569670f9421428603b072740e8a8f819be199503ce7f")

    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
