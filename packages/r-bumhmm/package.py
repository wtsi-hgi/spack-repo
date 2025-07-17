# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBumhmm(RPackage):
    """Computational pipeline for computing probability of modification from structure probing experiment data

    This is a probabilistic modelling pipeline for computing per- nucleotide posterior probabilities of modification from the data collected in structure probing experiments. The model supports multiple experimental replicates and empirically corrects coverage- and sequence-dependent biases. The model utilises the measure of a "drop-off rate" for each nucleotide, which is compared between replicates through a log-ratio (LDR). The LDRs between control replicates define a null distribution of variability in drop-off rate observed by chance and LDRs between treatment and control replicates gets compared to this distribution. Resulting empirical p-values (probability of being "drawn" from the null distribution) are used as observations in a Hidden Markov Model with a Beta-Uniform Mixture model used as an emission model. The resulting posterior probabilities indicate the probability of a nucleotide of having being modified in a structure probing experiment.
    """

    bioc = "BUMHMM"

    version("1.32.0", commit="ec1985bda853e5490498f5e13d68a2beaf25191b")
    version("1.26.0", commit="586babd0524b558e70f1e781c5dfec79bdfe521e")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
