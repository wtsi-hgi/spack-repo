# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrbasedbi(RPackage):
    """DBI to construct LRBase-related package

    Interface to construct LRBase package (LRBase.XXX.eg.db).
    """

    bioc = "LRBaseDbi"

    version("2.18.1", commit="1976965f68f6695bb81645e2e1d04a8bb711cc37")
    version("2.12.1", commit="12fa36355b50e6dd3a5c573b9bf3a23c036aa30b")
    version("2.12.0", md5="4ed780d2b26059691bd1a1e859ca5003")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
