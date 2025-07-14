# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhdf5client(RPackage):
	"""Access HDF5 content from HDF Scalable Data Service

	This package provides functionality for reading data from HDF Scalable Data Service from within R.  The HSDSArray function bridges from HSDS to the user via the DelayedArray interface.  Bioconductor manages an open HSDS instance graciously provided by John Readey of the HDF Group.
	"""
	
	bioc = "rhdf5client"

	version("1.30.0", commit="756fa5e608c3fa8b97bd3d81cb6276fea7541e5f")
	version("1.24.0", commit="4f73a042b882dcdb8474b2e0ee98bedfb269e92d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
