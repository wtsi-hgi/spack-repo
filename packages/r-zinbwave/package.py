# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZinbwave(RPackage):
	"""Zero-Inflated Negative Binomial Model for RNA-Seq Data

	Implements a general and flexible zero-inflated negative binomial model that can be used to provide a low-dimensional representations of single-cell RNA-seq data. The model accounts for zero inflation (dropouts), over-dispersion, and the count nature of the data. The model also accounts for the difference in library sizes and optionally for batch effects and/or other covariates, avoiding the need for pre-normalize the data.
	"""
	
	bioc = "zinbwave" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/zinbwave_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/zinbwave/zinbwave_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="310c8758283aa31b017606514d6f4b0f81336b21cc1f1fd357f300965feae8d2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
