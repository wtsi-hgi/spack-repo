# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSirad(RPackage):
	"""Functions for Calculating Daily Solar Radiation and
Evapotranspiration

	Calculating daily global solar radiation at horizontal surface using several well-known models (i.e. Angstrom-Prescott, Supit-Van Kappel, Hargreaves, Bristow and Campbell, and Mahmood-Hubbard), and model calibration based on ground-truth data, and (3) model auto-calibration. The FAO Penmann-Monteith equation to calculate evapotranspiration is also included.
	"""
	
	homepage = "http://sirad.r-forge.r-project.org/"
	cran = "sirad" 

	version("2.3-3", md5="df3646a78cc46127dfb811a15ce5efee")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
