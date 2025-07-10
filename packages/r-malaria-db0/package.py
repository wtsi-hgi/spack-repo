# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMalariaDb0(RPackage):
	"""Base Level Annotation databases for malaria

	Base annotation databases for malaria, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "malaria.db0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/malaria.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/malaria.db0/malaria.db0_3.18.0.tar.gz"]

	version("3.18.0", sha256="c3ed112c9ab2dd28bbe95d1f8c4a2ef24edd1111d43d3bbb294a68bef691e2fe", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/malaria.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

