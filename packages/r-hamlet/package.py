# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHamlet(RPackage):
	"""Hierarchical Optimal Matching and Machine Learning Toolbox

	Various functions and algorithms are provided here for solving optimal matching tasks in the context of preclinical cancer studies. Further, various helper and plotting functions are provided for unsupervised and supervised machine learning as well as longitudinal mixed-effects modeling of tumor growth response patterns.
	"""
	
	cran = "hamlet" 

	version("0.9.6", md5="6a38d99aef0ca6ade8b529c4eeb287bf")

	depends_on("r@3:", type=("build", "run"))
