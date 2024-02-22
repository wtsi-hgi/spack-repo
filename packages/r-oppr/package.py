# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROppr(RPackage):
	"""Optimal Project Prioritization

	A decision support tool for prioritizing conservation projects.
    Prioritizations can be developed by maximizing expected feature richness,
    expected phylogenetic diversity, the number of features that meet
    persistence targets, or identifying a set of projects that meet persistence
    targets for minimal cost. Constraints (e.g. lock in specific actions) and
    feature weights can also be specified to further customize prioritizations.
    After defining a project prioritization problem, solutions can be obtained
    using exact algorithms, heuristic algorithms, or random processes. In
    particular, it is recommended to install the 'Gurobi' optimizer (available
    from <https://www.gurobi.com>) because it can identify optimal solutions
    very quickly. Finally, methods are provided for comparing different
    prioritizations and evaluating their benefits. For more information, see
    Hanson et al. (2019) <doi:10.1111/2041-210X.13264>.
	"""
	
	homepage = "https://prioritizr.github.io/oppr/"
	cran = "oppr" 

	version("1.0.4", md5="46248e30448e7b2604f1f3c0e8cf6d07")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-uuid@0.1.2:", type=("build", "run"))
	depends_on("r-proto@1:", type=("build", "run"))
	depends_on("r-cli@1.0.1:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-ape@5.2:", type=("build", "run"))
	depends_on("r-tidytree@0.3.3:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-viridislite@0.3:", type=("build", "run"))
	depends_on("r-lpsolveapi@5.5.2.0.17:", type=("build", "run"))
	depends_on("r-withr@2.4.1:", type=("build", "run"))
	depends_on("r-rcpp@0.12.19:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.100.5:", type=("build", "run"))
	depends_on("r-rcppprogress@0.4.1:", type=("build", "run"))
