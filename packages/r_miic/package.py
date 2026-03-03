# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiic(RPackage):
	"""Learning Causal or Non-Causal Graphical Models Using Information
Theory

	We report an information-theoretic method which learns a large
    class of causal or non-causal graphical models from purely observational
    data, while including the effects of unobserved latent variables, commonly
    found in many datasets. Starting from a complete graph, the method
    iteratively removes dispensable edges, by uncovering significant information
    contributions from indirect paths, and assesses edge-specific confidences
    from randomization of available data. The remaining edges are then oriented
    based on the signature of causality in observational data. This approach can
    be applied on a wide range of datasets and provide new biological insights
    on regulatory networks from single cell expression data, genomic alterations
    during tumor development and co-evolving residues in protein structures.
    For more information you can refer to:
    Cabeli et al. PLoS Comp. Bio. 2020 <doi:10.1371/journal.pcbi.1007866>,
    Verny et al. PLoS Comp. Bio. 2017 <doi:10.1371/journal.pcbi.1005662>.
	"""
	
	homepage = "https://github.com/miicTeam/miic_R_package"
	cran = "miic" 

	version("1.5.3", md5="d35846a4814055be6049a4353e09a6bf")

	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
