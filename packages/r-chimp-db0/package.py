# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChimpDb0(RPackage):
	"""Base Level Annotation databases for chimp

	Base annotation databases for chimp, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "chimp.db0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/chimp.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/chimp.db0/chimp.db0_3.18.0.tar.gz"]

	version("3.18.0", sha256="f5a5276b1433174c422776469f005cd69c559179bf883fe21f38340a4789bef8", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/chimp.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

