# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharedobject(RPackage):
	"""Sharing R objects across multiple R processes without memory duplication

	This package is developed for facilitating parallel computing in R. It is capable to create an R object in the shared memory space and share the data across multiple R processes. It avoids the overhead of memory dulplication and data transfer, which make sharing big data object across many clusters possible.
	"""
	
	bioc = "SharedObject" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SharedObject_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SharedObject/SharedObject_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="77fd00f492f1dd9fbb6821c9f01172aa271c7f7440c4a787627810794098fc21")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
