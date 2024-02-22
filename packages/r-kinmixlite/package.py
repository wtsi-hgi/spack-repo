# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKinmixlite(RPackage):
	"""Inference About Relationships from DNA Mixtures

	Methods for inference about relationships between contributors to a DNA mixture and 
  other individuals of known genotype: a basic example would be testing whether a contributor to 
  a mixture is the father of a child of known genotype. This provides most of the functionality
  of the 'KinMix' package, but with some loss of efficiency and restriction on problem size,
  as the latter uses 'RHugin' as the Bayes net engine, while this package uses 'gRain'.
  The package implements the methods introduced in 
  Green, P. J. and Mortera, J. (2017) <doi:10.1016/j.fsigen.2017.02.001> and 
  Green, P. J. and Mortera, J. (2021) <doi:10.1111/rssc.12498>.
	"""
	
	homepage = "https://petergreenweb.wordpress.com/kinmix/"
	cran = "KinMixLite" 

	version("2.1.0", md5="941c877e3a86ef2b1d892438d5eaa8a4")

	depends_on("r-dnamixtureslite", type=("build", "run"))
	depends_on("r-graven", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ribd", type=("build", "run"))
	depends_on("r-pedtools", type=("build", "run"))
