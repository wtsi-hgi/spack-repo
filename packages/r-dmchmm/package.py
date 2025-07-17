# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmchmm(RPackage):
    """Differentially Methylated CpG using Hidden Markov Model

    A pipeline for identifying differentially methylated CpG sites using Hidden Markov Model in bisulfite sequencing data. DNA methylation studies have enabled researchers to understand methylation patterns and their regulatory roles in biological processes and disease. However, only a limited number of statistical approaches have been developed to provide formal quantitative analysis. Specifically, a few available methods do identify differentially methylated CpG (DMC) sites or regions (DMR), but they suffer from limitations that arise mostly due to challenges inherent in bisulfite sequencing data. These challenges include: (1) that read-depths vary considerably among genomic positions and are often low; (2) both methylation and autocorrelation patterns change as regions change; and (3) CpG sites are distributed unevenly. Furthermore, there are several methodological limitations: almost none of these tools is capable of comparing multiple groups and/or working with missing values, and only a few allow continuous or multiple covariates. The last of these is of great interest among researchers, as the goal is often to find which regions of the genome are associated with several exposures and traits. To tackle these issues, we have developed an efficient DMC identification method based on Hidden Markov Models (HMMs) called “DMCHMM” which is a three-step approach (model selection, prediction, testing) aiming to address the aforementioned drawbacks.
    """

    bioc = "DMCHMM"

    version("1.30.1", commit="c7fad5865a8306f67755c569a7770f0a30d1ed9f")
    version("1.24.0", commit="bae8dc82632d5a4f34d252e51f32977c5be8f234")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-fdrtool", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-multcomp", type=("build", "run"))
    depends_on("r-calibrate", type=("build", "run"))
