# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMugaexampledata(RPackage):
    """Example {M}ouse {U}niversal {G}enotyping {A}rray data for genome reconstruction and quantitative trait locus mapping.

    This package contains example data for the MUGA array that is used by the R package DOQTL.
    """

    bioc = "MUGAExampleData"

    version("1.28.0", commit="89efdba2bc2c0c77e438e1b3dcc02f4cf2c1e470")
    version("1.22.0", commit="3414f294576a5255e91a04855e75ea370f44a0d7")

    depends_on("r@2.10:", type=("build", "run"))
