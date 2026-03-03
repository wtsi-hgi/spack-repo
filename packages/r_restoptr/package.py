# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestoptr(RPackage):
	"""Ecological Restoration Planning

	
  Flexible framework for ecological restoration planning. It aims to identify priority areas for restoration efforts using optimization algorithms (based on Justeau-Allaire et al. 2021 <doi:10.1111/1365-2664.13803>). Priority areas can be identified by maximizing landscape indices, such as the effective mesh size (Jaeger 2000 <doi:10.1023/A:1008129329289>), or the integral index of connectivity (Pascual-Hortal & Saura 2006 <doi:10.1007/s10980-006-0013-z>). Additionally, constraints can be used to ensure that priority areas exhibit particular characteristics (e.g., ensure that particular places are not selected for restoration, ensure that priority areas form a single contiguous network). Furthermore, multiple near-optimal solutions can be generated to explore multiple options in restoration planning. The package leverages the 'Choco-solver' software to perform optimization using constraint programming (CP) techniques (<https://choco-solver.org/>).
	"""
	
	homepage = "https://dimitri-justeau.github.io/restoptr/"
	cran = "restoptr" 

	version("1.0.6", md5="bf5368e10fb777086ac20d714e062985")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-terra@1.6.17:", type=("build", "run"))
	depends_on("r-rjava@1.0.6:", type=("build", "run"))
	depends_on("r-units@0.8.0:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-crayon@1.4.1:", type=("build", "run"))
	depends_on("openjdk@11.0.12:", type=("build", "link", "run"))
