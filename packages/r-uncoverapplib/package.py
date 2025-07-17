# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUncoverapplib(RPackage):
    """Interactive graphical application for clinical assessment of sequence coverage at the base-pair level

    a Shiny application containing a suite of graphical and statistical tools to support clinical assessment of low coverage regions.It displays three web pages each providing a different analysis module: Coverage analysis, calculate AF by allele frequency app and binomial distribution. uncoverAPP provides a statisticl summary of coverage given target file or genes name.
    """

    homepage = "https://github.com/Manuelaio/uncoverappLib"
    bioc = "uncoverappLib"

    version("1.18.0", commit="ec9f8b60f337a2a73cb31ae99e68cc862df6a434")
    version("1.12.0", commit="2424917ba226e144f82a392d39ad05bf7f15d66e")

    depends_on("r-markdown", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-shinybs", type=("build", "run"))
    depends_on("r-shinywidgets", type=("build", "run"))
    depends_on("r-shinycssloaders", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-homo-sapiens", type=("build", "run"))
    depends_on("r-openxlsx", type=("build", "run"))
    depends_on("r-condformat", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-rappdirs", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
    depends_on("r-rlist", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-ensdb-hsapiens-v75", type=("build", "run"))
    depends_on("r-ensdb-hsapiens-v86", type=("build", "run"))
    depends_on("r-organismdbi", type=("build", "run"))
    depends_on("r-processx", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
