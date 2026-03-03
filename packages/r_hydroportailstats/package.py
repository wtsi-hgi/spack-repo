# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydroportailstats(RPackage):
	"""'HydroPortail' Statistical Functions

	Statistical functions used in the French 'HydroPortail' <https://hydro.eaufrance.fr/>.
    This includes functions to estimate distributions, quantile curves and uncertainties, along with various other utilities.
    Technical details are available (in French) in Renard (2016) <https://hal.inrae.fr/hal-02605318>.
	"""
	
	cran = "HydroPortailStats" 

	version("1.0.3", md5="a73cfb53882d206038997cf089e8b0b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
