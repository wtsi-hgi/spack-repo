# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArraymvout(RPackage):
	"""multivariate outlier detection for expression array QA

	This package supports the application of diverse quality metrics to AffyBatch instances, summarizing these metrics via PCA, and then performing parametric outlier detection on the PCs to identify aberrant arrays with a fixed Type I error rate
	"""
	
	bioc = "arrayMvout" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/arrayMvout_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/arrayMvout/arrayMvout_1.60.0.tar.gz"]

	version("1.60.0", sha256="1ffebe64d66f20ebb221ab344f546f2c5338d1e94def83a32a56bde841d7737c")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-parody", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-mdqc", type=("build", "run"))
	depends_on("r-affycontam", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))
