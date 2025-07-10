# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene10StV1frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type mogene.1.0.st.v1frmavecs

	This package was created by frmaTools version 1.13.0.
	"""
	
	bioc = "mogene.1.0.st.v1frmavecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mogene.1.0.st.v1frmavecs_1.1.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mogene.1.0.st.v1frmavecs/mogene.1.0.st.v1frmavecs_1.1.0.tar.gz"]

	version("1.1.0", sha256="50099ee6e82215ec9f33f57e6274ab6910bf0376350400a71c55c376de549e02")

	depends_on("r@2.10:", type=("build", "run"))

