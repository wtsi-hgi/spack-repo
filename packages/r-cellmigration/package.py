# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellmigration(RPackage):
	"""Track Cells, Analyze Cell Trajectories and Compute Migration Statistics

	Import TIFF images of fluorescently labeled cells, and track cell movements over time. Parallelization is supported for image processing and for fast computation of cell trajectories. In-depth analysis of cell trajectories is enabled by 15 trajectory analysis functions.
	"""
	
	homepage = "https://github.com/ocbe-uio/cellmigRation/"
	bioc = "cellmigRation" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cellmigRation_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cellmigRation/cellmigRation_1.10.0.tar.gz"]

	version("1.10.0", md5="61fc4a74a41e132fc3b760bc444ee5d4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-fme", type=("build", "run"))
	depends_on("r-spatialtools", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-vioplot", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
