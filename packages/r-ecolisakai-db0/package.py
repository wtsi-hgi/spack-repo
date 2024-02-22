# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolisakaiDb0(RPackage):
	"""Base Level Annotation databases for E coli Sakai Strain

	Base annotation databases for E coli Sakai Strain, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "ecoliSakai.db0" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ecoliSakai.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ecoliSakai.db0/ecoliSakai.db0_3.18.0.tar.gz"]

	version("3.18.0", md5="2afd28e9062d869d37e3d65dbe410bcb", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ecoliSakai.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

	# annotation