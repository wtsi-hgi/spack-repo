# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM3dexampledata(RPackage):
    """M3Drop Example Data

    Example data for M3Drop package.
    """

    bioc = "M3DExampleData"

    version("1.34.0", commit="46aef0fbb76f1e71be8d4c462363641a55246fbd")
    version("1.28.0", commit="0cf50a6bc14b6dc229bfd41f5555b9895acd4968")

    depends_on("r@3.3:", type=("build", "run"))
