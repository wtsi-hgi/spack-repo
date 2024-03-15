# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetectr(RPackage):
	"""Change Point Detection

	Time series analysis of network connectivity. Detects and visualizes change points between networks.
    Methods included in the package are discussed in depth in Baek, C., Gates, K. M., Leinwand, B., Pipiras, V. (2021)
    "Two sample tests for high-dimensional auto-covariances" <doi:10.1016/j.csda.2020.107067>
    and Baek, C., Gampe, M., Leinwand B., Lindquist K., Hopfinger J. and Gates K. (2023)
    “Detecting functional connectivity changes in fMRI data” <doi:10.1007/s11336-023-09908-7>.
	"""
	
	homepage = "https://github.com/crbaek/detectR"
	cran = "detectR" 

	version("0.3.0", md5="6caf0d5f1efe0e0dc0580c654cdee32d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-logconcdead", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
