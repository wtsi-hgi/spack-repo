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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rhdf5client_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rhdf5client/rhdf5client_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="441b144dc73c4c34a84e9d335781679b8b57d2bf1d84656d41b7ad5782975156")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
