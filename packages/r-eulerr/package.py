# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REulerr(RPackage):
	"""Area-Proportional Euler and Venn Diagrams with Ellipses

	Generate area-proportional Euler diagrams
    using numerical optimization. An Euler diagram is a generalization of a Venn
    diagram, relaxing the criterion that all interactions need to be
    represented. Diagrams may be fit with ellipses and circles via
    a wide range of inputs and can be visualized in numerous ways.
	"""
	
	homepage = "https://github.com/jolars/eulerr"
	cran = "eulerr" 

	version("7.0.2", md5="20709a5b9ff83b575d5e034a3f568fb5")
	version("7.0.1", md5="67ce0dab076b2e6361f1b2da3debde59")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-polyclip", type=("build", "run"))
	depends_on("r-polylabelr", type=("build", "run"))
	depends_on("r-rcpp@0.12.12:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
