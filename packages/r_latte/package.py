# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatte(RPackage):
	"""Interface to 'LattE' and '4ti2'

	Back-end connections to 'LattE' (<https://www.math.ucdavis.edu/~latte>) 
	for counting lattice points and integration inside convex polytopes and 
	'4ti2' (<http://www.4ti2.de/>) for algebraic, geometric, and combinatorial 
	problems on linear spaces and front-end tools facilitating their use in the 
	'R' ecosystem.
	"""
	
	homepage = "https://github.com/dkahle/latte"
	cran = "latte" 

	version("0.2.1", md5="e3d612ac53c4a24f73957fe8ddf1e4cb")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mpoly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("latte", type=("build", "link", "run"))
