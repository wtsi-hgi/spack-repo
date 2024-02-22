# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConogive(RPackage):
	"""Congeneric Normal-Ogive Model

	The congeneric normal-ogive model is a popular model for 
   psychometric data (McDonald, R. P. (1997) <doi:10.1007/978-1-4757-2691-6_15>).
   This model estimates the model, calculates theoretical and concrete 
   reliability coefficients, and predicts the latent variable of the model. 
   This is the companion package to Moss (2020) <doi:10.31234/osf.io/nvg5d>.
	"""
	
	homepage = "https://github.com/JonasMoss/conogive"
	cran = "conogive" 

	version("1.0.0", md5="d62017e181bb14a565ed325ddc563405")

	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
