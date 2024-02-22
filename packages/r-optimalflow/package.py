# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimalflow(RPackage):
	"""optimalFlow

	Optimal-transport techniques applied to supervised flow cytometry gating.
	"""
	
	bioc = "optimalFlow" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/optimalFlow_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/optimalFlow/optimalFlow_1.14.0.tar.gz"]

	version("1.14.0", md5="c66127dc23a70fdcfd651543ea596329")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-optimalflowdata", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-flowmeans", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
