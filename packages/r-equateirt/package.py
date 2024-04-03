# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquateirt(RPackage):
	"""IRT Equating Methods

	Computation of direct, chain and average (bisector) equating coefficients with 
  standard errors using Item Response Theory (IRT) methods for dichotomous items 
  (Battauz (2013) <doi:10.1007/s11336-012-9316-y>, 
  Battauz (2015) <doi:10.18637/jss.v068.i07>). 
  Test scoring can be performed by true score equating and observed score equating methods. 
  DIF detection can be performed using a Wald-type test  
  (Battauz (2019) <doi:10.1007/s10260-018-00442-w>).
  The package includes tests to access the stability of the equating transformations
  (Battauz(2022) <doi:10.1111/stan.12277>).
	"""
	
	cran = "equateIRT" 

	version("2.3.0", md5="e33238f3f9c59812163abbd3ef2ab939")
	version("2.4.0", md5="41573bf1cfa67d0550103ad900466959")

	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
