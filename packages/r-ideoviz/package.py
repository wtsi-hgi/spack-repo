# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdeoviz(RPackage):
    """Plots data (continuous/discrete) along chromosomal ideogram

    Plots data associated with arbitrary genomic intervals along chromosomal ideogram.
    """

    bioc = "IdeoViz"

    version("1.44.0", commit="5928e144a23b225c5d0083793fee3ee18536aa6c")
    version(
        "1.37.0",
        sha256="7a387e5276f66a103101ff98925a550bc035194ca7be4c5b71e529f84acc0aae",
    )

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
