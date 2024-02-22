# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrr(RPackage):
	"""Various Coefficients of Interrater Reliability and Agreement

	Coefficients of Interrater Reliability and Agreement for
        quantitative, ordinal and nominal data: ICC, Finn-Coefficient,
        Robinson's A, Kendall's W, Cohen's Kappa, ...
	"""
	
	homepage = "https://www.r-project.org"
	cran = "irr" 

	version("0.84.1", md5="802ae19d1fc45cede1afafb5012cfdf0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
