# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouseDb0(RPackage):
	"""Base Level Annotation databases for mouse

	Base annotation databases for mouse, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "mouse.db0" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mouse.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mouse.db0/mouse.db0_3.18.0.tar.gz"]

	version("3.18.0", md5="1ef6bb1d25e53443871e0e8c975b36c0", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mouse.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation