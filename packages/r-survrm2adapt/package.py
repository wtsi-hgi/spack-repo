# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvrm2adapt(RPackage):
	"""Flexible and Coherent Test/Estimation Procedure Based on
Restricted Mean Survival Times

	Estimates the restricted mean survival time (RMST) with the time window [0, tau], where tau is adaptively selected from the procedure, proposed by Horiguchi et al. (2018) <doi:10.1002/sim.7661>. It also estimates the RMST with the time window [tau1, tau2], where tau1 is adaptively selected from the procedure, proposed by Horiguchi et al. (2023) <doi:10.1002/sim.9662>.
	"""
	
	cran = "survRM2adapt" 

	version("1.1.0", md5="0ae7ff1e8b3a047613e4aebfb124007c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
