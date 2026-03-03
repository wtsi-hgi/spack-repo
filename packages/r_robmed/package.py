# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobmed(RPackage):
	"""(Robust) Mediation Analysis

	Perform mediation analysis via the fast-and-robust bootstrap test ROBMED (Alfons, Ates & Groenen, 2022a; <doi:10.1177/1094428121999096>), as well as various other methods. Details on the implementation and code examples can be found in Alfons, Ates, and Groenen (2022b) <doi:10.18637/jss.v103.i13>.
	"""
	
	homepage = "https://github.com/aalfons/robmed"
	cran = "robmed" 

	version("1.0.2", md5="e49c1414bb23f5d8131a9898c4cfeee7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-robustbase@0.92.7:", type=("build", "run"))
	depends_on("r-boot@1.3.20:", type=("build", "run"))
	depends_on("r-quantreg@5.36:", type=("build", "run"))
	depends_on("r-sn@1.5.4:", type=("build", "run"))
