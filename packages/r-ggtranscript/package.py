# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtranscript(RPackage):
    """Visualizing Transcript Structure and Annotation Using 'ggplot2'

    Provides geoms and helper functions that simplify plotting transcript
    structures within the 'ggplot2' framework so users can combine exon, intron,
    and junction annotations to build publication-ready figures.
    """

    homepage = "https://github.com/dzhang32/ggtranscript"
    git = "https://github.com/dzhang32/ggtranscript.git"
    license = "MIT"

    version("20240824", commit="682a0df688ad242fa262d0b0557bf973dc202787")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
