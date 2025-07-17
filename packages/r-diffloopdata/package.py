# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffloopdata(RPackage):
    """Example ChIA-PET Datasets for the diffloop Package

    ChIA-PET example datasets and additional data for use with the diffloop package.
    """

    bioc = "diffloopdata"

    version("1.36.0", commit="a0b0834a9886d6fc3f0aa046fb2e177f0a9cb8cb")
    version("1.30.0", commit="b7371d193bffef7ce62bb7a360c670b29282f9b6")
