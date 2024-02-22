# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModestm(RPackage):
	"""Mode Estimation, Even in the Multimodal Case

	Function ModEstM() is the only one of this package, it estimates the modes of an empirical univariate distribution. It relies on the stats::density() function, even for input control. Due to very good performance of the density estimation, computation time is not an issue. The multiple modes are handled using dplyr::group_by(). For conditions and rates of convergences, see Eddy (1980) <doi:10.1214/aos/1176345080>.
	"""
	
	cran = "ModEstM" 

	version("0.0.1", md5="0eeb92e1751c5d2901a140a264e28d00")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
