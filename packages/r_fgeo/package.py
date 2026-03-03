# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgeo(RPackage):
	"""Analyze Forest Diversity and Dynamics

	To help you access, transform, analyze, and
    visualize ForestGEO data, we developed a collection of R packages
    (<https://forestgeo.github.io/fgeo/>). This package, in particular,
    helps you to install and load the entire package-collection with a
    single R command, and provides convenient ways to find relevant
    documentation. Most commonly, you should not worry about the
    individual packages that make up the package-collection as you can
    access all features via this package. To learn more about ForestGEO
    visit <http://www.forestgeo.si.edu/>.
	"""
	
	homepage = "http://forestgeo.github.io/fgeo"
	cran = "fgeo" 

	version("1.1.4", md5="a02ca0ec68266d47cdcfcb001e345a7b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cli@1.1:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.1:", type=("build", "run"))
	depends_on("r-fgeo-analyze@1.1.10:", type=("build", "run"))
	depends_on("r-fgeo-plot@1.1.6:", type=("build", "run"))
	depends_on("r-fgeo-tool@1.2.4:", type=("build", "run"))
	depends_on("r-fgeo-x@1.1.3:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.3.4:", type=("build", "run"))
	depends_on("r-rstudioapi@0.10:", type=("build", "run"))
