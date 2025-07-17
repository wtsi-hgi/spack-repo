# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsMm10(RPackage):
    """RnBeads.mm10

    Automatically generated RnBeads annotation package for the assembly mm10.
    """

    bioc = "RnBeads.mm10"

    version("2.16.0", commit="ab7a2a9d4fca34d689aeee44dacadc2cff1cb8c0")
    version("2.10.0", commit="d4c15d06b47f6b161df8aecbcc68c8df15276144")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
