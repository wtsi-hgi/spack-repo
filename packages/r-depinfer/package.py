# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepinfer(RPackage):
    """Inferring tumor-specific cancer dependencies through integrating ex-vivo drug response assays and drug-protein profiling

    DepInfeR integrates two experimentally accessible input data matrices: the drug sensitivity profiles of cancer cell lines or primary tumors ex-vivo (X), and the drug affinities of a set of proteins (Y), to infer a matrix of molecular protein dependencies of the cancers (ß). DepInfeR deconvolutes the protein inhibition effect on the viability phenotype by using regularized multivariate linear regression. It assigns a “dependence coefficient” to each protein and each sample, and therefore could be used to gain a causal and accurate understanding of functional consequences of genomic aberrations in a heterogeneous disease, as well as to guide the choice of pharmacological intervention for a specific cancer type, sub-type, or an individual patient. For more information, please read out preprint on bioRxiv: https://doi.org/10.1101/2022.01.11.475864.
    """

    bioc = "DepInfeR"

    version("1.12.0", commit="aa3280195c532ce1effd5f23dff0dbe61a34580c")
    version("1.6.0", commit="97f4dc3d14241e6dc0c452f80d9f680e08a703d0")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
