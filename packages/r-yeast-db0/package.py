# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastDb0(RPackage):
	"""Base Level Annotation databases for yeast

	Base annotation databases for yeast, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "yeast.db0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/yeast.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/yeast.db0/yeast.db0_3.18.0.tar.gz"]

	version("3.18.0", md5="483043596daee94866843e6a43dcf538", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/yeast.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation