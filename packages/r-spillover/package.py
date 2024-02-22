# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpillover(RPackage):
	"""Spillover/Connectedness Index Based on VAR Modelling

	A user-friendly tool for estimating both total and directional connectedness spillovers based on Diebold and Yilmaz (2009, 2012). It also provides the user with rolling estimation for total and net indices. User can find both orthogonalized and generalized versions for each kind of measures. See Diebold and Yilmaz (2009, 2012) find them at  <doi:10.1111/j.1468-0297.2008.02208.x> and <doi:10.1016/j.ijforecast.2011.02.006>.
	"""
	
	cran = "Spillover" 

	version("0.1.0.3", md5="67e76daf671ad6ce2c63c69af14c82e7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-fastsom", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
