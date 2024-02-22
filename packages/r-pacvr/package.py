# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPacvr(RPackage):
	"""Plastome Assembly Coverage Visualization

	Visualizes the coverage depth of a complete plastid genome as well as the equality of its inverted repeat regions in relation to the circular, quadripartite genome structure and the location of individual genes. For more information, please see Gruenstaeudl and Jenke (2020) <doi:10.1186/s12859-020-3475-0>.
	"""
	
	homepage = "https://github.com/michaelgruenstaeudl/PACVr"
	cran = "PACVr" 

	version("1.0.7", md5="10345787023970e9aff81113a1efc456")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biostrings@2.48:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicalignments@1.18.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-read-gb@2.2:", type=("build", "run"))
	depends_on("r-rcircos@1.2:", type=("build", "run"))
