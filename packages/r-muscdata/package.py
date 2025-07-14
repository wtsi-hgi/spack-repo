# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuscdata(RPackage):
	"""Multi-sample multi-group scRNA-seq data

	Data package containing a collection of multi-sample multi-group scRNA-seq datasets in SingleCellExperiment Bioconductor object format.
	"""
	
	homepage = "https://github.com/HelenaLC/muscData"
	bioc = "muscData"

	version("1.22.0", commit="497deeba5758db04f26113873b3c6cb97a041b62")
	version("1.16.0", commit="30ae3fc37dadb46f34adf98f8ccf00ed520cb307")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))

