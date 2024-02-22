# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAphid(RPackage):
	"""Analysis with Profile Hidden Markov Models

	Designed for the development and application of
    hidden Markov models and profile HMMs for biological sequence analysis. 
    Contains functions for multiple and pairwise sequence alignment, 
    model construction and parameter optimization, file import/export,
    implementation of the forward, backward and Viterbi algorithms for 
    conditional sequence probabilities, tree-based sequence weighting, 
    and sequence simulation. 
    Features a wide variety of potential applications including 
    database searching, gene-finding and annotation, phylogenetic 
    analysis and sequence classification.
    Based on the models and algorithms described in Durbin et 
    al (1998, ISBN: 9780521629713).
	"""
	
	homepage = "https://github.com/shaunpwilkinson/aphid"
	cran = "aphid" 

	version("1.3.5", md5="04dcb0245fe84efdfb2611f1c6563b4c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-kmer@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
