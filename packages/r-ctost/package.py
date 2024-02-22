# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtost(RPackage):
	"""Finite Sample Correction of the Two One-Sided Tests in the
Univariate Framework

	A system containing easy-to-use tools to compute the bioequivalence assessment in the univariate framework using the methods proposed in Boulaguiem et al. (2023) <doi:10.1101/2023.03.11.532179>.
	"""
	
	homepage = "https://github.com/yboulag/cTOST"
	cran = "cTOST" 

	version("1.0.0", md5="8f26fe1991a35385e8ba83ea80451da6")

	depends_on("r-powertost", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-owenq", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
