# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbwa(RPackage):
    """R wrapper for BWA-backtrack and BWA-MEM aligners

    Provides an R wrapper for BWA alignment algorithms. Both BWA-backtrack and BWA-MEM are available. Convenience function to build a BWA index from a reference genome is also provided. Currently not supported for Windows machines.
    """

    homepage = "https://github.com/crisprVerse/Rbwa"
    bioc = "Rbwa"
    urls = [
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rbwa_1.6.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rbwa/Rbwa_1.6.0.tar.gz",
    ]

    version("1.12.0", tag="RELEASE_3_21")
    version("1.6.0", sha256="797e5ba373240a25af5201dfa69be6bed3ab5d6f1a48f4a8a2e96e35ca3e6772")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("zlib-api", type=("build", "run", "link"))

    def patch(self):
        # the clean step messes up with parallel making
        # since we use Spack there is no need to clean
        filter_file("all:$(PROG) ../inst/bwa clean", "all:$(PROG) ../inst/bwa", "src/Makefile", string=True)
