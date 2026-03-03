# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunpca(RPackage):
	"""Functional Principal Component Analysis

	Functional principal component analysis under the Linear Mixed Models representation of smoothing splines. The method utilizes the Demmler-Reinsch basis and assumes error independence. For more details see: F. Rosales (2016) <https://ediss.uni-goettingen.de/handle/11858/00-1735-0000-0028-87F9-6>.
	"""
	
	cran = "funpca" 

	version("9.0", md5="a53e4aeb667c6e2df36aec22b686cb82")

	depends_on("r-brobdingnag", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
