# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHireewas(RPackage):
	"""Detection of cell-type-specific risk-CpG sites in epigenome-wide association studies

	In epigenome-wide association studies, the measured signals for each sample are a mixture of methylation profiles from different cell types. The current approaches to the association detection only claim whether a cytosine-phosphate-guanine (CpG) site is associated with the phenotype or not, but they cannot determine the cell type in which the risk-CpG site is affected by the phenotype. We propose a solid statistical method, HIgh REsolution (HIRE), which not only substantially improves the power of association detection at the aggregated level as compared to the existing methods but also enables the detection of risk-CpG sites for individual cell types. The "HIREewas" R package is to implement HIRE model in R.
	"""
	
	bioc = "HIREewas" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HIREewas_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HIREewas/HIREewas_1.20.0.tar.gz"]

	version("1.20.0", md5="fd57bb11c16b2d194d7950ce0d918899")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
