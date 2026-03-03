# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLncfinder(RPackage):
	"""LncRNA Identification and Analysis Using Heterologous Features

	Long non-coding RNAs identification and analysis. Default models are trained with human, mouse and wheat datasets by employing SVM. Features are based on intrinsic composition of sequence, EIIP value (electron-ion interaction pseudopotential), and secondary structure. This package can also extract other classic features and build new classifiers. Reference: Han SY., Liang YC., Li Y., et al. (2018) <doi:10.1093/bib/bby065>.
	"""
	
	homepage = "https://bmbl.bmi.osumc.edu/lncfinder/"
	cran = "LncFinder" 

	version("1.1.5", md5="5490dbe7aa34f9012a34977a9ec6fd3a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-seqinr@2.1.3:", type=("build", "run"))
	depends_on("r-e1071@1:", type=("build", "run"))
	depends_on("r-caret@6.0.71:", type=("build", "run"))
