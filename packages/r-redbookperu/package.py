# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedbookperu(RPackage):
	"""Access and Analyze the Data from the Red Book of Endemic Plants
of Peru

	Access and analysis of data from `The Red Book of Endemic Plants of Peru` León, B., Roque, J., Ulloa, C., Jorgensen, P.M., Pitman, N., Cano, A. (2006)<doi:10.15381/rpb.v13i2.1782> providing taxonomic, geographic, and conservation information about Peru's endemic plant species. The package offers functions to check species inclusion, obtain updated taxonomic details, and explore the dataset.
	"""
	
	homepage = "https://github.com/PaulESantos/redbookperu"
	cran = "redbookperu" 

	version("0.0.2", md5="6668288332b95cc695907dbb81c594d7")

	depends_on("r@2.10:", type=("build", "run"))
