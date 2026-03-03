# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadnsx(RPackage):
	"""Read 'Blackrock-Microsystems' Files ('NEV', 'NSx')

	Loads 'Blackrock' <https://blackrockneurotech.com> neural signal 
    data files into the memory, provides utility tools to extract the data into 
    common formats such as plain-text 'tsv' and 'HDF5'.
	"""
	
	homepage = "http://dipterix.org/readNSx/"
	cran = "readNSx" 

	version("0.0.4", md5="65dd693a9ee21f9b0dc4b7cd1ccf4cb0")
	version("0.0.3", md5="3ecc816256ce4f7520587b2ee620d5b4")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
	depends_on("r-hdf5r", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("hdf5@1.8.13:", type=("build", "link", "run"))
