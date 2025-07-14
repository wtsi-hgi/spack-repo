# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialexperiment(RPackage):
	"""S4 Class for Spatially Resolved -omics Data

	Defines an S4 class for storing data from spatial -omics experiments. The class extends SingleCellExperiment to support storage and retrieval of additional information from spot-based and molecule-based platforms, including spatial coordinates, images, and image metadata. A specialized constructor function is included for data from the 10x Genomics Visium platform.
	"""
	
	homepage = "https://github.com/drighelli/SpatialExperiment"
	bioc = "SpatialExperiment"

	version("1.18.1", commit="a7ee918d268f620311f4434fc4bb1e73d33dcf37")
	version("1.12.0", commit="46a1748b1cbe0317202077b018781c0f19355740")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
