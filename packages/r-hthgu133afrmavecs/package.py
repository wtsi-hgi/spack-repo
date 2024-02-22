# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133afrmavecs(RPackage):
	"""Vectors used by frma for microarrays of type hthgu133a

	This package was created by frmaTools version 1.19.3 and hgu133ahsentrezgcdf version 19.0.0.
	"""
	
	bioc = "hthgu133afrmavecs" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hthgu133afrmavecs_1.3.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hthgu133afrmavecs/hthgu133afrmavecs_1.3.0.tar.gz"]

	version("1.3.0", md5="be3f3d67a94dca3b080c184fba5ff6d8")

	depends_on("r@2.10:", type=("build", "run"))

	# annotation