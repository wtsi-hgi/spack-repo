# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsobayes(RPackage):
    """IsoBayes: Single Isoform protein inference Method via Bayesian Analyses

    IsoBayes is a Bayesian method to perform inference on single protein isoforms. Our approach infers the presence/absence of protein isoforms, and also estimates their abundance; additionally, it provides a measure of the uncertainty of these estimates, via: i) the posterior probability that a protein isoform is present in the sample; ii) a posterior credible interval of its abundance. IsoBayes inputs liquid cromatography mass spectrometry (MS) data, and can work with both PSM counts, and intensities. When available, trascript isoform abundances (i.e., TPMs) are also incorporated: TPMs are used to formulate an informative prior for the respective protein isoform relative abundance. We further identify isoforms where the relative abundance of proteins and transcripts significantly differ. We use a two-layer latent variable approach to model two sources of uncertainty typical of MS data: i) peptides may be erroneously detected (even when absent); ii) many peptides are compatible with multiple protein isoforms. In the first layer, we sample the presence/absence of each peptide based on its estimated probability of being mistakenly detected, also known as PEP (i.e., posterior error probability). In the second layer, for peptides that were estimated as being present, we allocate their abundance across the protein isoforms they map to. These two steps allow us to recover the presence and abundance of each protein isoform.
    """

    homepage = "https://github.com/SimoneTiberi/IsoBayes"
    bioc = "IsoBayes"

    version("1.6.1", commit="6c4ba7eaa0f2e273957ed9df1715cd20936311ed")
    version("1.0.1", commit="0abca1bcf630d5394befde38ed7d9cc87c8efc18")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-dorng", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-iterators", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-hdinterval", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
