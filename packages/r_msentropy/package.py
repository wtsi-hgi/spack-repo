# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsentropy(RPackage):
	"""Spectral Entropy for Mass Spectrometry Data

	Clean the MS/MS spectrum, calculate spectral entropy, unweighted entropy similarity, and entropy similarity for mass spectrometry data. The entropy similarity is a novel similarity measure for MS/MS spectra which outperform the widely used dot product similarity in compound identification. For more details, please refer to the paper: Yuanyue Li et al. (2021) "Spectral entropy outperforms MS/MS dot product similarity for small-molecule compound identification" <doi:10.1038/s41592-021-01331-z>.
	"""
	
	homepage = "https://github.com/YuanyueLi/MSEntropy"
	cran = "msentropy" 

	version("0.1.4", md5="2ed7f0b24ab7fef0335edbb65da9ee52")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
