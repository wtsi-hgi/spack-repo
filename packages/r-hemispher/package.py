# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHemispher(RPackage):
	"""Processing Hemispherical Canopy Images

	Import and classify canopy fish-eye images, estimate angular gap fraction and derive canopy attributes like leaf area index and openness.  Additional information is provided in the study by Chianucci F., Macek M. (2023) <doi:10.1016/j.agrformet.2023.109470>.
	"""
	
	cran = "hemispheR" 

	version("1.1.3", md5="ddcdf4e640cd8de46454a9f4e90ea0c0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-terra@1.7.55:", type=("build", "run"))
	depends_on("r-autothresholdr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-dismo", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
