# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProthmm(RPackage):
	"""Protein Feature Extraction from Profile Hidden Markov Models

	Calculates a comprehensive list of features from profile hidden Markov models (HMMs) of proteins. 
    Adapts and ports features for use with HMMs instead of Position Specific Scoring Matrices, in order to take 
    advantage of more accurate multiple sequence alignment by programs such as 'HHBlits' Remmert et al. (2012) 
    <DOI:10.1038/nmeth.1818> and 'HMMer' Eddy (2011) <DOI:10.1371/journal.pcbi.1002195>. Features calculated by 
    this package can be used for protein fold classification, protein structural class prediction, 
    sub-cellular localization and protein-protein interaction, among other tasks. Some examples of features 
    extracted are found in Song et al. (2018) <DOI:10.3390/app8010089>, Jin & Zhu (2021) <DOI:10.1155/2021/8629776>, 
    Lyons et al. (2015) <DOI:10.1109/tnb.2015.2457906> and Saini et al. (2015) <DOI:10.1016/j.jtbi.2015.05.030>.
	"""
	
	homepage = "https://semran9.github.io/protHMM/"
	cran = "protHMM" 

	version("0.1.1", md5="ec628c9c328ba6639ab8c2f9adc439ba")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-phontools", type=("build", "run"))
