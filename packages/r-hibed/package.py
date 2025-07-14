# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHibed(RPackage):
	"""HiBED

	Hierarchical deconvolution for extensive cell type resolution in the human brain using DNA methylation. The HiBED deconvolution estimates proportions up to 7 cell types (GABAergic neurons, glutamatergic neurons, astrocytes, microglial cells, oligodendrocytes, endothelial cells, and stromal cells) in bulk brain tissues.
	"""
	
	homepage = "https://github.com/SalasLab/HiBED"
	bioc = "HiBED" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/HiBED_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/HiBED/HiBED_1.0.0.tar.gz"]

	version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="7c035a50659cd7b55b701c8b86945ba937531ef4ee3a60375beb970bdf954cb1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flowsorted-blood-epic", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-flowsorted-dlpfc-450k", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

