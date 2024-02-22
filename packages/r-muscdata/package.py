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
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/muscData_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/muscData/muscData_1.16.0.tar.gz"]

	version("1.16.0", md5="f34c376f88f97c98d4aac5490b45bc24")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))

	# experiment