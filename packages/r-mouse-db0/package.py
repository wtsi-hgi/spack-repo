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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse.db0/mouse.db0_3.18.0.tar.gz"]

	version("3.18.0", sha256="1ef3ab54e9b8ccdb6e49f8f43903290ced46a5bf9fac7d520a6f2e9ce7925924", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

