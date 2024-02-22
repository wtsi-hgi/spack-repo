# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaehbMeBeta(RPackage):
	"""SAE with Measurement Error using HB under Beta Distribution

	Implementation of Small Area Estimation (SAE) using Hierarchical Bayesian (HB) Method when auxiliary variable measured with error under Beta Distribution. The 'rjags' package is employed to obtain parameter estimates. For the references, see J.N.K & Molina (2015) <doi:10.1002/9781118735855>, Ybarra and Sharon (2008) <doi:10.1093/biomet/asn048>, and Ntzoufras (2009, ISBN-10: 1118210352).
	"""
	
	homepage = "https://github.com/ratihrodliyah/saeHB.ME.beta"
	cran = "saeHB.ME.beta" 

	version("1.1.0", md5="625cee760c5b0ee2a0809db98ed99f3c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
