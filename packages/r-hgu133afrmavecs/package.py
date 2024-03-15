# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133afrmavecs(RPackage):
	"""Vectors used by frma for microarrays of type hgu133a

	This package was created by frmaTools version 1.19.3 and hgu133ahsentrezgcdf version 19.0.0.
	"""
	
	bioc = "hgu133afrmavecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133afrmavecs_1.5.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133afrmavecs/hgu133afrmavecs_1.5.0.tar.gz"]

	version("1.5.0", md5="85034ab02491f5b3699d210cef50812d")

	depends_on("r@2.10:", type=("build", "run"))

	# annotation