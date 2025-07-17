# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWavcluster(RPackage):
    """Sensitive and highly resolved identification of RNA-protein interaction sites in PAR-CLIP data

    The package provides an integrated pipeline for the analysis of PAR-CLIP data. PAR-CLIP-induced transitions are first discriminated from sequencing errors, SNPs and additional non-experimental sources by a non- parametric mixture model. The protein binding sites (clusters) are then resolved at high resolution and cluster statistics are estimated using a rigorous Bayesian framework. Post-processing of the results, data export for UCSC genome browser visualization and motif search analysis are provided. In addition, the package allows to integrate RNA-Seq data to estimate the False Discovery Rate of cluster detection. Key functions support parallel multicore computing. Note: while wavClusteR was designed for PAR-CLIP data analysis, it can be applied to the analysis of other NGS data obtained from experimental procedures that induce nucleotide substitutions (e.g. BisSeq).
    """

    bioc = "wavClusteR"

    version("2.42.0", commit="fbb85b2bc7753a1a30d4d32cad885aacf5b14d33")
    version("2.36.0", commit="bec165394e95fb3ee904d54de1ee7a8bfab5c3de")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
    depends_on("r-iranges@2.13.12:", type=("build", "run"))
    depends_on("r-biostrings@2.47.6:", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-genomicfeatures@1.31.3:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))
    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
