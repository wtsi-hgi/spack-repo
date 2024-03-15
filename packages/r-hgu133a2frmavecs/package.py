# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133a2frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type hgu133a2

	This package was created by frmaTools version 1.19.3 and hgu133ahsentrezgcdf version 19.0.0.
	"""
	
	bioc = "hgu133a2frmavecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133a2frmavecs_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133a2frmavecs/hgu133a2frmavecs_1.2.0.tar.gz"]

	version("1.2.0", md5="4bf8cf5cbaf288ce0a9618d764c87044")

	depends_on("r@2.10:", type=("build", "run"))

	# annotation