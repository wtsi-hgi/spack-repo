# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnclustomics(RPackage):
	"""Bayesian Network-Based Clustering of Multi-Omics Data

	Unsupervised Bayesian network-based clustering of multi-omics data. Both binary and continuous data types
    are allowed as inputs. The package serves a dual purpose: it clusters (patient) samples and learns the multi-omics networks that characterize discovered
    clusters. Prior network knowledge (e.g., public interaction databases) can be included via blacklisting and 
    penalization matrices. For clustering, the EM algorithm is employed. For structure search at the M-step,
    the Bayesian approach is used. The output includes membership assignments of samples, cluster-specific MAP networks, and posterior probabilities
    of all edges in the discovered networks. In addition to likelihood, AIC and BIC scores are returned. They can be used for choosing the number
    of clusters.
    References:
    P. Suter et al. (2021) <doi:10.1101/2021.12.16.473083>,
    J. Kuipers and P. Suter and G. Moffa (2022) <doi:10.1080/10618600.2021.2020127>,
    J. Kuipers et al. (2018) <doi:10.1038/s41467-018-06867-x>.
	"""
	
	cran = "bnClustOmics" 

	version("1.1.1", md5="b6f76fca2ed504c2c585a166aa6a5fd9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bidag", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
