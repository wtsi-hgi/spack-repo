# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepwisetest(RPackage):
	"""Multiple Testing Method to Control Generalized Family-Wise Error
Rate and False Discovery Proportion

	Collection of stepwise procedures to conduct multiple hypotheses testing. The details of the stepwise algorithm can be found in Romano and Wolf (2007) <DOI:10.1214/009053606000001622> and Hsu, Kuan, and Yen (2014) <DOI:10.1093/jjfinec/nbu014>.
	"""
	
	cran = "StepwiseTest" 

	version("1.0", md5="86187c602cdc6dfe2d8ebb94411d8e77")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
