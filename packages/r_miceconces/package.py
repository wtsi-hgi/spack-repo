# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiceconces(RPackage):
	"""Analysis with the Constant Elasticity of Substitution (CES)
Function

	Tools for econometric analysis and economic modelling
   with the traditional two-input Constant Elasticity of Substitution (CES) function
   and with nested CES functions with three and four inputs.
   The econometric estimation can be done by the Kmenta approximation,
   or non-linear least-squares
   using various gradient-based or global optimisation algorithms.
   Some of these algorithms can constrain the parameters to certain ranges,
   e.g. economically meaningful values.
   Furthermore, the non-linear least-squares estimation
   can be combined with a grid-search for the rho-parameter(s).
   The estimation methods are described in Henningsen et al. (2021)
   <doi:10.4337/9781788976480.00030>.
	"""
	
	homepage = "http://www.micEcon.org"
	cran = "micEconCES" 

	version("1.0-2", md5="49f72f8076e5a793d89e9826607bcb62")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-minpack-lm@1.1.4:", type=("build", "run"))
	depends_on("r-deoptim@2.0.4:", type=("build", "run"))
	depends_on("r-car@2.0.0:", type=("build", "run"))
	depends_on("r-systemfit@1.0.0:", type=("build", "run"))
	depends_on("r-micecon@0.6.1:", type=("build", "run"))
	depends_on("r-misctools@0.6.1:", type=("build", "run"))
