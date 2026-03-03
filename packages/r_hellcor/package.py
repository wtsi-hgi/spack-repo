# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHellcor(RPackage):
	"""The Hellinger Correlation

	Empirical value of the Hellinger correlation, a measure of dependence between
	     two continuous random variables. More details can be found in Geenens and Lafaye De Micheaux (2019) <arXiv:1810.10276v4>. 
	"""
	
	cran = "HellCor" 

	version("1.3", md5="c360b2b62ab252ec6002213c281fb13e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
