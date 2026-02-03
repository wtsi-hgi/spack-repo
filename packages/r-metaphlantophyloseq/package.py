# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaphlantophyloseq(RPackage):
    """A simple R package to convert MetaPhlAn 4 output profiles to a phyloseq object."""

    homepage = "https://jrotzetter.github.io/metaphlanToPhyloseq/"
    url = "https://github.com/jrotzetter/metaphlanToPhyloseq/archive/refs/tags/v0.2.0.tar.gz"


    license("MIT")

    version("0.2.0", sha256="eccf4aa2ff841216f68ec933209f5d702173213f21e984aa563279fb51831592")

    depends_on("r-dplyr@1.1.4:")
    depends_on("r-phyloseq@1.46.0:")
    depends_on("r-r-utils")

