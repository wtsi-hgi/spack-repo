# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemuxsnp(RPackage):
    """scRNAseq demultiplexing using cell hashing and SNPs

    This package assists in demultiplexing scRNAseq data using both cell hashing and SNPs data. The SNP profile of each group os learned using high confidence assignments from the cell hashing data. Cells which cannot be assigned with high confidence from the cell hashing data are assigned to their most similar group based on their SNPs. We also provide some helper function to optimise SNP selection, create training data and merge SNP data into the SingleCellExperiment framework.
    """

    homepage = "https://github.com/michaelplynch/demuxSNP"
    bioc = "demuxSNP"

    version("1.6.0", commit="294315c20918b455e92ae9881792b03e6c3a28f8")
    version("1.0.0", commit="1af04e30f2b6fe4264a28fea374305294a2d8bff")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-ensembldb", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-class", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-demuxmix", type=("build", "run"))
    depends_on("r-combinat", type=("build", "run"))
    depends_on("r-kernelknn", type=("build", "run"))
