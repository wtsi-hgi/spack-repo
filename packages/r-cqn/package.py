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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cqn_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cqn/cqn_1.48.0.tar.gz"]

    version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="c8f951f85b5397d631e55a87c07a672fc50fdd6474b544484631463f5471b660")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-nor1mix", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
