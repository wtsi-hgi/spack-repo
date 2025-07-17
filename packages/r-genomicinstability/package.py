# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicinstability(RPackage):
    """Genomic Instability estimation for scRNA-Seq

    This package contain functions to run genomic instability analysis (GIA) from scRNA-Seq data. GIA estimates the association between gene expression and genomic location of the coding genes. It uses the aREA algorithm to quantify the enrichment of sets of contiguous genes (loci-blocks) on the gene expression profiles and estimates the Genomic Instability Score (GIS) for each analyzed cell.
    """

    homepage = "https://github.com/DarwinHealth/genomicInstability"
    bioc = "genomicInstability"

    version("1.14.0", commit="9b0831bfe28a7bda917d7e568322eb2846d3efcd")
    version("1.8.0", commit="188233e23f9c35f09aee7657755bd8ce77183dec")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-mixtools", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
