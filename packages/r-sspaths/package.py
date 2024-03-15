# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSspaths(RPackage):
	"""ssPATHS: Single Sample PATHway Score

	This package generates pathway scores from expression data for single samples after training on a reference cohort. The score is generated by taking the expression of a gene set (pathway) from a reference cohort and performing linear discriminant analysis to distinguish samples in the cohort that have the pathway augmented and not. The separating hyperplane is then used to score new samples.
	"""
	
	bioc = "ssPATHS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ssPATHS_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ssPATHS/ssPATHS_1.16.0.tar.gz"]

	version("1.16.0", md5="121909c57596e3cd0d817cac2deb22c9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-dml", type=("build", "run"))
	depends_on("r-mess", type=("build", "run"))
