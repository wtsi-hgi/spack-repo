# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWormDb0(RPackage):
	"""Base Level Annotation databases for worm

	Base annotation databases for worm, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "worm.db0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/worm.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/worm.db0/worm.db0_3.18.0.tar.gz"]

	version("3.18.0", md5="67be1277b5ae184558259ac720a5741e", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/worm.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation