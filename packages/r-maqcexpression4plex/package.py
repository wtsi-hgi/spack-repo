# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaqcexpression4plex(RPackage):
    """Sample Expression Data - MAQC / HG18 - NimbleGen

    Data from human (HG18) 4plex NimbleGen array. It has 24k genes with 3 60mer probes per gene.
    """

    bioc = "maqcExpression4plex"

    version("1.52.0", commit="7cd26dc3a55586289401cc928c789ac67f9edb38")
    version("1.46.0", commit="b67c28d378ab1bdbd7e4d9f9c4e84200a3f9ac22")
