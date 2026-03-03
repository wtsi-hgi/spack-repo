# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcpmodgeneral(RPackage):
	"""A Supplement to the 'DoseFinding' Package for the General Case

	Analyzes non-normal data via the Multiple Comparison Procedures and Modeling approach (MCP-Mod). Many functions rely on the 'DoseFinding' package. This package makes it so the user does not need to provide or calculate the mu vector and S matrix. Instead, the user typically supplies the data in its raw form, and this package will calculate the needed objects and passes them into the 'DoseFinding' functions. If the user wishes to primarily use the functions provided in the 'DoseFinding' package, a singular function (prepareGen()) will provide mu and S. The package currently handles power analysis and the MCP-Mod procedure for negative binomial, Poisson, and binomial data. The MCP-Mod procedure can also be applied to survival data, but power analysis is not available.
	Bretz, F., Pinheiro, J. C., and Branson, M. (2005) <doi:10.1111/j.1541-0420.2005.00344.x>.
	Buckland, S. T., Burnham, K. P. and Augustin, N. H. (1997) <doi:10.2307/2533961>.
	Pinheiro, J. C., Bornkamp, B., Glimm, E. and Bretz, F. (2014) <doi:10.1002/sim.6052>.
	"""
	
	cran = "MCPModGeneral" 

	version("0.1-1", md5="60c7c05d5d7890226cf0702cda791d11")

	depends_on("r-dosefinding", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
