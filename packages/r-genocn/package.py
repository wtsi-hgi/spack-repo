# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenocn(RPackage):
    """genotyping and copy number study tools

    Simultaneous identification of copy number states and genotype calls for regions of either copy number variations or copy number aberrations
    """

    bioc = "genoCN"

    version("1.60.0", commit="d875c71eb4c04137e24dbdeb0edb55ed0dcd7735")
    version("1.54.0", commit="98243384501c57e00e793fdb9f9148920c74ca5e")
