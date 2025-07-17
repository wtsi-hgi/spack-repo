# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcyjs(RPackage):
    """Display and manipulate graphs in cytoscape.js

    Interactive viewing and exploration of graphs, connecting R to Cytoscape.js, using websockets.
    """

    bioc = "RCyjs"

    version("2.30.0", commit="4b23fe7000bbbb55fc03cd87dcb63f112d9556cd")
    version("2.24.0", commit="51a82aaa4c46af97a9a954a9ae335e53db298ef4")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-browserviz@2.7.18:", type=("build", "run"))
    depends_on("r-graph@1.56:", type=("build", "run"))
    depends_on("r-httpuv@1.5:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-base64enc", type=("build", "run"))
