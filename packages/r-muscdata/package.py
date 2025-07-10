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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/muscData_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/muscData/muscData_1.16.0.tar.gz"]

	version("1.16.0", sha256="aaf36d5799af4ec978eae1635b0966a6e0951a8f69738292b7d391f953695506")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))

