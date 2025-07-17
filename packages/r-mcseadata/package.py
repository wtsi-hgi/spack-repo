# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcseadata(RPackage):
    """Data package for mCSEA package

    Data objects necessary to some mCSEA package functions. There are also example data objects to illustrate mCSEA package functionality.
    """

    bioc = "mCSEAdata"

    version("1.28.0", commit="479e3886a064f24fe06ba4d6ca3c90032b82c2d2")
    version("1.22.0", commit="93aea4c24ced94e1223ad0da4644449592c9c02c")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
