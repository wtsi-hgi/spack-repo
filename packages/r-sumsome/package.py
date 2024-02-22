# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSumsome(RPackage):
	"""Permutation True Discovery Guarantee by Sum-Based Tests

	It allows to quickly perform permutation-based closed testing by sum-based global tests, and construct lower confidence bounds for the TDP, simultaneously over all subsets of hypotheses. As a main feature, it produces simultaneous lower confidence bounds for the proportion of active voxels in different clusters for fMRI cluster analysis. Details may be found in Vesely, Finos, and Goeman (2020) <arXiv:2102.11759>.
	"""
	
	homepage = "https://github.com/annavesely/sumSome"
	cran = "sumSome" 

	version("1.1.0", md5="5cc6564990c1a25cccfdb299b1ee3933")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pari", type=("build", "run"))
	depends_on("r-aribrain", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
