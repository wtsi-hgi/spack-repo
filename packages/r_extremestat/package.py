# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremestat(RPackage):
	"""Extreme Value Statistics and Quantile Estimation

	Fit, plot and compare several (extreme value) distribution functions. 
    Compute (truncated) distribution quantile estimates and plot return periods on a linear scale.
   	On the fitting method, see Asquith (2011): Distributional Analysis with L-moment Statistics [...]  ISBN 1463508417.
	"""
	
	homepage = "https://github.com/brry/extremeStat"
	cran = "extremeStat" 

	version("1.5.9", md5="445d15a0d9dfd04ff6d59627c27ea4bd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lmomco@2.2.5:", type=("build", "run"))
	depends_on("r-berryfunctions@1.15.6:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-evir", type=("build", "run"))
	depends_on("r-ismev", type=("build", "run"))
	depends_on("r-fextremes", type=("build", "run"))
	depends_on("r-extremes", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-renext", type=("build", "run"))
