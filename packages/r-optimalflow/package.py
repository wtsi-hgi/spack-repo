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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/optimalFlow_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/optimalFlow/optimalFlow_1.14.0.tar.gz"]

	version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="b97a0a2aa8a800e4fc9c83a266e90a6cf1aae9ed8032185efdf6e18e886c1c3e")

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
