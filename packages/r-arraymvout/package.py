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

	version("1.66.0", commit="2099184584bc0bb730e236f7b65ea4d37c7bc4d0")
	version("1.60.0", commit="f24566a929ab83f086cc062d2a785230ab930cc9")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-parody", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-mdqc", type=("build", "run"))
	depends_on("r-affycontam", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))
