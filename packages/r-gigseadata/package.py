# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGigseadata(RPackage):
	"""Gene set collections for the GIGSEA package

	The gene set collection used for the GIGSEA package.
	"""
	
	bioc = "GIGSEAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/GIGSEAdata_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/GIGSEAdata/GIGSEAdata_1.20.0.tar.gz"]

	version("1.20.0", sha256="bf7597cd68872e42abe02d52483dcbc4761ed61a314ffa9cf0e9c99507893a62")

	depends_on("r@3.5:", type=("build", "run"))

