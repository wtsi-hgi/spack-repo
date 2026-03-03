# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedbuildr(RPackage):
	"""Pedigree Reconstruction

	Reconstruct pedigrees from genotype data, by optimising the
    likelihood over all possible pedigrees subject to given restrictions.
    Tailor-made plots facilitate evaluation of the output. This package is
    part of the 'pedsuite' ecosystem for pedigree analysis. In
    particular, it imports 'pedprobr' for calculating pedigree likelihoods
    and 'forrel' for estimating pairwise relatedness.
	"""
	
	homepage = "https://github.com/magnusdv/pedbuildr"
	cran = "pedbuildr" 

	version("0.3.0", md5="042370bc1bcf3a5e74f2b755173ff0e7")

	depends_on("r-pedtools@2.2:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-forrel@1.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pedmut", type=("build", "run"))
	depends_on("r-pedprobr", type=("build", "run"))
	depends_on("r-ribd", type=("build", "run"))
