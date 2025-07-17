# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReder(RPackage):
    """Interactive visualization and manipulation of nested networks

    RedeR is an R-based package combined with a stand-alone Java application for interactive visualization and manipulation of nested networks.
    """

    homepage = "http://genomebiology.com/2012/13/4/R29"
    bioc = "RedeR"

    version("3.4.0", commit="7a6a9f585de70267e54c9a73df6712ac9f03d0c3")
    version("2.6.1", commit="0a91264d8282983b97f2ef2beec444b59dc76ad8")
    version("2.6.0", md5="033b5763d95dc222256a4ef85b7e3a99")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("openjdk@11:", type=("build", "link", "run"))
