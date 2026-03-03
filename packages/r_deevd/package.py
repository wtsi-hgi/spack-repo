# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeevd(RPackage):
	"""Density Estimation by Extreme Value Distributions

	Provides mean squared error (MSE) and plot the kernel densities related to extreme value distributions with their estimated values.
    By using Gumbel and Weibull Kernel. See Salha et al. (2014) <doi:10.4236/ojs.2014.48061> and Khan and Akbar (2021) <doi:10.4236/ojs.2021.112018 >.
	"""
	
	homepage = "https://CRAN.R-project.org/package=DEEVD"
	cran = "DEEVD" 

	version("1.2.3", md5="f8a8cc2b5413f131662eba3df64ebd06")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
