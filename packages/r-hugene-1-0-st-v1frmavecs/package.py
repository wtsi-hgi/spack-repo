# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene10StV1frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type hugene.1.0.st.v1frmavecs

	This package was created by frmaTools version 1.13.0.
	"""
	
	bioc = "hugene.1.0.st.v1frmavecs" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hugene.1.0.st.v1frmavecs_1.1.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hugene.1.0.st.v1frmavecs/hugene.1.0.st.v1frmavecs_1.1.0.tar.gz"]

	version("1.1.0", md5="711a69e6fa6dd3737a90615222416dfc")

	depends_on("r@2.10:", type=("build", "run"))

	# annotation