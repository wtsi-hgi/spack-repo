# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpqdep(RPackage):
	"""Testing for Spatial Independence of Qualitative Data in Cross
Section

	Testing for Spatial Dependence of Qualitative Data in Cross Section. The list of functions includes join-count tests, Q test, spatial scan test, similarity test and spatial runs test. The methodology of these models can be found in <doi:10.1007/s10109-009-0100-1> and <doi:10.1080/13658816.2011.586327>.
	"""
	
	homepage = "https://f8l5h9.github.io/spqdep/"
	cran = "spqdep" 

	version("0.1.3.2", md5="80315958fd595e939816d365af5b6c4b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom@0.7.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gt@0.2.2:", type=("build", "run"))
	depends_on("r-rgeoda@0.0.8.6:", type=("build", "run"))
	depends_on("r-gtools@3.8.2:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-igraph@1.2.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-matrix@1.2.18:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rsample@0.0.8:", type=("build", "run"))
	depends_on("r-sp@1.4.5:", type=("build", "run"))
	depends_on("r-spatialreg@1.1.8:", type=("build", "run"))
	depends_on("r-spdep@1.1.3:", type=("build", "run"))
	depends_on("r-sf@0.9.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-lwgeom@0.2.8:", type=("build", "run"))
