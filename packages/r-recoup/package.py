# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecoup(RPackage):
    """An R package for the creation of complex genomic profile plots

    recoup calculates and plots signal profiles created from short sequence reads derived from Next Generation Sequencing technologies. The profiles provided are either sumarized curve profiles or heatmap profiles. Currently, recoup supports genomic profile plots for reads derived from ChIP-Seq and RNA-Seq experiments. The package uses ggplot2 and ComplexHeatmap graphics facilities for curve and heatmap coverage profiles respectively.
    """

    homepage = "https://github.com/pmoulos/recoup"
    bioc = "recoup"

    version("1.36.0", commit="8a4864d75a5c45ca3c0b55ce4f2d3b0f1b76c384")
    version("1.30.0", commit="0d1e96b2feff097c41268ec5190e0337b2d4ce9f")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
