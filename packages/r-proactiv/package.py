# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProactiv(RPackage):
    """Estimate Promoter Activity from RNA-Seq data

    Most human genes have multiple promoters that control the expression of different isoforms. The use of these alternative promoters enables the regulation of isoform expression pre-transcriptionally. Alternative promoters have been found to be important in a wide number of cell types and diseases. proActiv is an R package that enables the analysis of promoters from RNA-seq data. proActiv uses aligned reads as input, and generates counts and normalized promoter activity estimates for each annotated promoter. In particular, proActiv accepts junction files from TopHat2 or STAR or BAM files as inputs. These estimates can then be used to identify which promoter is active, which promoter is inactive, and which promoters change their activity across conditions. proActiv also allows visualization of promoter activity across conditions.
    """

    homepage = "https://github.com/GoekeLab/proActiv"
    bioc = "proActiv"

    version("1.18.0", commit="6e9d41c9f8a9cff765494756c255fb5a09f1cf1f")
    version("1.12.0", commit="a55e732ed8d6ffca83700d68eb80dff6af87b8bb")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
