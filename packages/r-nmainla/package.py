# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmainla(RPackage):
	"""Network Meta-Analysis using Integrated Nested Laplace
Approximations

	Performs network meta-analysis using integrated nested Laplace approximations ('INLA') 
             which is described in Guenhan, Held, and Friede (2018) <doi:10.1002/jrsm.1285>. 
             Includes methods to assess the heterogeneity and inconsistency in the network. 
             Contains more than ten different network meta-analysis dataset. 
             'INLA' package can be obtained from <https://www.r-inla.org>. 
	"""
	
	homepage = "https://github.com/gunhanb/nmaINLA"
	cran = "nmaINLA" 

	version("1.1.0", md5="8ba1f54b39cc96b7c3b95ebc794bef07")

	depends_on("r@2.10:", type=("build", "run"))
