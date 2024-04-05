# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlyDb0(RPackage):
	"""Base Level Annotation databases for fly

	Base annotation databases for fly, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "fly.db0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/fly.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/fly.db0/fly.db0_3.18.0.tar.gz"]

	version("3.18.0", md5="49722b8a538d02f71631a418b92c44d7", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/fly.db0_3.18.0.tar.gz")
	version("3.18.0", md5="49722b8a538d02f71631a418b92c44d7", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/fly.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

