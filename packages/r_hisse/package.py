# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHisse(RPackage):
	"""Hidden State Speciation and Extinction

	Sets up and executes a HiSSE model (Hidden State Speciation and Extinction) on a phylogeny and character sets to test for hidden shifts in trait dependent rates of diversification. Beaulieu and O'Meara (2016) <doi:10.1093/sysbio/syw022>.
	"""
	
	cran = "hisse" 

	version("2.1.11", md5="5036c2faeb0c48ca1a977643a8256d78")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-subplex", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-diversitree", type=("build", "run"))
	depends_on("r-paleotree", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-treesim", type=("build", "run"))
	depends_on("r-corhmm", type=("build", "run"))
