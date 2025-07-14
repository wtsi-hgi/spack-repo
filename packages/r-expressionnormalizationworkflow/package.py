# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpressionnormalizationworkflow(RPackage):
	"""Gene Expression Normalization Workflow

	An extensive, customized expression normalization workflow incorporating Supervised Normalization of Microarryas(SNM), Surrogate Variable Analysis(SVA) and Principal Variance Component Analysis to identify batch effects and remove them from the expression data to enhance the ability to detect the underlying biological signals.
	"""
	
	bioc = "ExpressionNormalizationWorkflow" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/ExpressionNormalizationWorkflow_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/ExpressionNormalizationWorkflow/ExpressionNormalizationWorkflow_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="6c774f657b6ca26fe24218a9a999f40f2313f3dc800b9376c1c9a1100e0d3ec8")

	depends_on("r-biobase@2.24:", type=("build", "run"))
	depends_on("r-limma@3.20.9:", type=("build", "run"))
	depends_on("r-lme4@1.1.7:", type=("build", "run"))
	depends_on("r-matrixstats@0.10.3:", type=("build", "run"))
	depends_on("r-pvca@1.4:", type=("build", "run"))
	depends_on("r-snm@1.12:", type=("build", "run"))
	depends_on("r-sva@3.10:", type=("build", "run"))
	depends_on("r-vsn@3.32:", type=("build", "run"))

