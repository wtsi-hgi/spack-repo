# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcopula(RPackage):
	"""Liouville Copulas

	Collections of functions allowing random number generations and
    estimation of 'Liouville' copulas, as described in Belzile and Neslehova (2017) <doi:10.1016/j.jmva.2017.05.008>.
	"""
	
	cran = "lcopula" 

	version("1.0.7", md5="703c8c3ee8a1efed9d8a0020cb8e12cc")

	depends_on("r-copula@0.999.12:", type=("build", "run"))
	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
