# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipxpressdata(RPackage):
    """ChIPXpress Pre-built Databases

    Contains pre-built mouse (GPL1261) and human (GPL570) database of gene expression profiles to be used for ChIPXpress ranking.
    """

    bioc = "ChIPXpressData"

    version("1.46.0", commit="9c3442ca7af5d1f92b25c8c07604fc71864e7051")
    version("1.40.0", md5="029086a630df9533dedea4babd28f0d7")

    depends_on("r-bigmemory", type=("build", "run"))
