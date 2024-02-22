# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsmooth(RPackage):
	"""Smooth quantile normalization

	Smooth quantile normalization is a generalization of quantile normalization, which is average of the two types of assumptions about the data generation process: quantile normalization and quantile normalization between groups.
	"""
	
	bioc = "qsmooth" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/qsmooth_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/qsmooth/qsmooth_1.18.0.tar.gz"]

	version("1.18.0", md5="471983d71a4b056b71b10fe15c3f7b1c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
