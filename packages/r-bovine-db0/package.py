# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBovineDb0(RPackage):
	"""Base Level Annotation databases for bovine

	Base annotation databases for bovine, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "bovine.db0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/bovine.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/bovine.db0/bovine.db0_3.18.0.tar.gz"]

	version("3.18.0", md5="658829797db74aec87af1914483d1af7", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/bovine.db0_3.18.0.tar.gz")
	version("3.18.0", md5="658829797db74aec87af1914483d1af7", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/bovine.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

