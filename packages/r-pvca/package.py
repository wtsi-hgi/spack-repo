# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvca(RPackage):
	"""Principal Variance Component Analysis (PVCA)

	This package contains the function to assess the batch sourcs by fitting all "sources" as random effects including two-way interaction terms in the Mixed Model(depends on lme4 package) to selected principal components, which were obtained from the original data correlation matrix. This package accompanies the book "Batch Effects and Noise in Microarray Experiements, chapter 12.
	"""
	
	bioc = "pvca" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pvca_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pvca/pvca_1.42.0.tar.gz"]

	version("1.42.0", sha256="6cf37e1570c5885f2e9980a8187f00ad5ecba66c94fea60850392dbcb0474d50")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
