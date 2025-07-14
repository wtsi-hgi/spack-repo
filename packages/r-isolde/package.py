# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsolde(RPackage):
	"""Integrative Statistics of alleLe Dependent Expression

	This package provides ISoLDE a new method for identifying imprinted genes. This method is dedicated to data arising from RNA sequencing technologies. The ISoLDE package implements original statistical methodology described in the publication below.
	"""
	
	homepage = "www.r-project.org"
	bioc = "ISoLDE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ISoLDE_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ISoLDE/ISoLDE_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="edbace394f931c0257a5c4e500be696a13183c30c1fa2383130808dd7ccb1dad")

	depends_on("r@3.3:", type=("build", "run"))
