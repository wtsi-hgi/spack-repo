# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCqn(RPackage):
	"""Conditional quantile normalization

	A normalization tool for RNA-Seq data, implementing the conditional quantile normalization method.
	"""
	
	bioc = "cqn" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cqn_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cqn/cqn_1.48.0.tar.gz"]

	version("1.48.0", md5="a72eb9ae5c393dec7ecc4f992d11328f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-nor1mix", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
