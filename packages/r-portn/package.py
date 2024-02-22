# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortn(RPackage):
	"""Portfolio Analysis for Nature

	The functions are designed to find the efficient mean-variance frontier or 
 portfolio weights for static portfolio (called  Markowitz portfolio) analysis in resource 
 economics or nature conservation. Using the nonlinear programming solver ('Rsolnp'), 
 this package deals with the quadratic minimization of the variance-covariances without 
 shorting (i.e., non-negative portfolio weights) studied in Ando and Mallory (2012) 
 <doi:10.1073/pnas.1114653109>. See the examples, testing versions, and more details from: 
 <https://github.com/ysd2004/portn>.
	"""
	
	homepage = "https://github.com/ysd2004/portn"
	cran = "portn" 

	version("1.0.0", md5="86f28b5418861eb312cd6be3396c51f4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
