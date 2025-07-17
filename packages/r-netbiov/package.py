# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetbiov(RPackage):
    """A package for visualizing complex biological network

    A package that provides an effective visualization of large biological networks
    """

    homepage = "http://www.bio-complexity.com"
    bioc = "netbiov"

    version("1.36.0", commit="9bedb5108ac6bb64229eb5b26581c3fa03b5df50")

    depends_on("r@3.1:", type=("build", "run"))
    depends_on("r-igraph@0.7.1:", type=("build", "run"))
