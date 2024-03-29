# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosum(RPackage):
	"""Moving Sum Based Procedures for Changes in the Mean

	Implementations of MOSUM-based statistical procedures and algorithms for detecting multiple changes in the mean. This comprises the MOSUM procedure for estimating multiple mean changes from Eichinger and Kirch (2018) <doi:10.3150/16-BEJ887> and the multiscale algorithmic extension from Cho and Kirch (2022) <doi:10.1007/s10463-021-00811-5>, as well as the bootstrap procedure for generating confidence intervals about the locations of change points as proposed in Cho and Kirch (2022) <doi:10.1016/j.csda.2022.107552>. See also Meier, Kirch and Cho (2021) <doi:10.18637/jss.v097.i08> which accompanies the R package.
	"""
	
	cran = "mosum" 

	version("1.2.7", md5="9813f64a9549078fb910eb40de03ff58")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
