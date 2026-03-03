# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKgen(RPackage):
	"""A Tool for Calculating Stoichiometric Equilibrium Constants (Ks)
for Seawater

	A unified software package simultaneously implemented in 'Python', 'R', and 'Matlab' providing a uniform and internally-consistent way of calculating stoichiometric equilibrium constants in modern and palaeo seawater as a function of temperature, salinity, pressure and the concentration of magnesium, calcium, sulphate, and fluorine.
	"""
	
	cran = "kgen" 

	version("0.3.1", md5="72209d31dd270ae2f8d41110be4b7bef")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rjson@0.2.21:", type=("build", "run"))
	depends_on("r-reticulate@1.26:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.3:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-pbapply@1.7:", type=("build", "run"))
	depends_on("r-data-table@1.14.6:", type=("build", "run"))
