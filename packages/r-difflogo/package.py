# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifflogo(RPackage):
    """DiffLogo: A comparative visualisation of biooligomer motifs

    DiffLogo is an easy-to-use tool to visualize motif differences.
    """

    homepage = "https://github.com/mgledi/DiffLogo/"
    bioc = "DiffLogo"

    version("2.32.0", commit="e640352b944e281f723299aec38abab5bafb27da")
    version("2.26.0", commit="cf17c71365444827dcee1b98010cabff205d9c3c")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-cba", type=("build", "run"))
