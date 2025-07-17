# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiobtreer(RPackage):
    """Using biobtree tool from R

    The biobtreeR package provides an interface to [biobtree](https://github.com/tamerh/biobtree) tool which covers large set of bioinformatics datasets and allows search and chain mappings functionalities.
    """

    homepage = "https://github.com/tamerh/biobtreeR"
    bioc = "biobtreeR"

    version("1.20.0", commit="36f5c12dd0af25614720c458c2416206a176f68a")
    version("1.14.0", commit="b97b0147a3b88a3109bd13cf1ed9c280925b5d4a")

    depends_on("r-httr", type=("build", "run"))
    depends_on("r-httpuv", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
