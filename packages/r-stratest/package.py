# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratest(RPackage):
	"""Strategy Estimation

	Variants of strategy estimation (Dal Bo & Frechette, 2011, <doi:10.1257/aer.101.1.411>), including the model with parameters for the choice probabilities of the strategies (Breitmoser, 2015, <doi:10.1257/aer.20130675>), and the model with individual level covariates for the selection of strategies by individuals (Dvorak & Fehrler, 2018, <doi:10.2139/ssrn.2986445>). 
	"""
	
	homepage = "https://github.com/fdvorak/stratEst"
	cran = "stratEst" 

	version("1.1.6", md5="292053fa75a9b9b0e1acc01c80789a1f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.900:", type=("build", "run"))
