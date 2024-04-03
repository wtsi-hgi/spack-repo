# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossover(RPackage):
	"""Analysis and Search of Crossover Designs

	Generate and analyse crossover designs from combinatorial or search algorithms as well as from literature and a GUI to
    access them.
	"""
	
	homepage = "https://github.com/kornl/Crossover/wiki"
	cran = "Crossover" 

	version("0.1-21", md5="209931798f536da383885c451f411a34")
	version("0.1-22", md5="ace5c665375194d1027092bf63f04d06")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-crossdes@1.1.1:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rjava@0.8.3:", type=("build", "run"))
	depends_on("r-commonjavajars@1.1:", type=("build", "run"))
	depends_on("r-rcpp@0.10.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.2:", type=("build", "run"))
	depends_on("r-javagd", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
