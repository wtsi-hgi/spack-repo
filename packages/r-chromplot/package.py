# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromplot(RPackage):
    """Global visualization tool of genomic data

    Package designed to visualize genomic data along the chromosomes, where the vertical chromosomes are sorted by number, with sex chromosomes at the end.
    """

    bioc = "chromPlot"

    version("1.36.0", commit="3c429c93631077d295db35b18858cf8cbe53c5a6")
    version("1.30.0", commit="7747c745e9fbdc249e166b9ed89b598cfdede997")

    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r@3.1:", type=("build", "run"))
