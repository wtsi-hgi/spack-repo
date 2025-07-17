# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariantexperiment(RPackage):
    """A RangedSummarizedExperiment Container for VCF/GDS Data with GDS Backend

    VariantExperiment is a Bioconductor package for saving data in VCF/GDS format into RangedSummarizedExperiment object. The high-throughput genetic/genomic data are saved in GDSArray objects. The annotation data for features/samples are saved in DelayedDataFrame format with mono-dimensional GDSArray in each column. The on-disk representation of both assay data and annotation data achieves on-disk reading and processing and saves memory space significantly. The interface of RangedSummarizedExperiment data format enables easy and common manipulations for high-throughput genetic/genomic data with common SummarizedExperiment metaphor in R and Bioconductor.
    """

    homepage = "https://github.com/Bioconductor/VariantExperiment"
    bioc = "VariantExperiment"

    version("1.22.0", commit="7470f43a557d5d276fc23b159f85895f347a8a42")
    version("1.16.0", commit="1e2834f96c4bb815871d118043d01bceaa4a1cbd")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-s4vectors@0.21.24:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.13:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-gdsarray@1.11.1:", type=("build", "run"))
    depends_on("r-delayeddataframe@1.6:", type=("build", "run"))
    depends_on("r-gdsfmt", type=("build", "run"))
    depends_on("r-snprelate", type=("build", "run"))
    depends_on("r-seqarray", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
