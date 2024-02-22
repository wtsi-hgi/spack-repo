# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrohaplot(RPackage):
	"""Microhaplotype Constructor and Visualizer

	A downstream bioinformatics tool to construct and assist 
    curation of microhaplotypes from short read sequences.
	"""
	
	homepage = "https://github.com/ngthomas/microhaplot"
	cran = "microhaplot" 

	version("1.0.1", md5="ed2492e55ffc55a172b0805fe22e6375")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dt@0.1:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-scales@0.4:", type=("build", "run"))
	depends_on("r-shiny@0.13.2:", type=("build", "run"))
	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-tidyr@0.4.1:", type=("build", "run"))
	depends_on("r-shinywidgets@0.4.3:", type=("build", "run"))
	depends_on("r-ggiraph@0.6:", type=("build", "run"))
