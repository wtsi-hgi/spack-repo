# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabelvector(RPackage):
    """Label Attributes for Atomic Vectors"""

    cran = "labelVector"

    version("0.1.2", md5="ad69706c30f9670a7d1c1896164856d6")

