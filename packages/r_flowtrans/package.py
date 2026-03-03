# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowtrans(RPackage):
	"""Parameter Optimization for Flow Cytometry Data Transformation

	Profile maximum likelihood estimation of parameters for flow cytometry data transformations.
	"""
	
	bioc = "flowTrans" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowTrans_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowTrans/flowTrans_1.54.0.tar.gz"]

	version("1.54.0", md5="d98daa4177e5f6b8cda8d8475e34c09a")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowviz", type=("build", "run"))
	depends_on("r-flowclust", type=("build", "run"))
