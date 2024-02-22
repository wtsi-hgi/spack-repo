# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignalhsmm(RPackage):
	"""Predict Presence of Signal Peptides

	Predicts the presence of signal peptides in eukaryotic protein
    using hidden semi-Markov models. The implemented algorithm can be accessed from
    both the command line and GUI.
	"""
	
	homepage = "https://github.com/michbur/signalhsmm"
	cran = "signalHsmm" 

	version("1.5", md5="07de8db09cd88eeff98f7c32852548ae")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
