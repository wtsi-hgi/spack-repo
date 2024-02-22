# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdf5rExtra(RPackage):
	"""Extensions for 'HDF5' R Interfaces

	Some methods to manipulate 'HDF5' files, extending the 'hdf5r' package. Reading and writing R objects to 'HDF5' formats follow the specification of 'AnnData' <https://anndata.readthedocs.io/en/latest/fileformat-prose.html>.
	"""
	
	homepage = "https://github.com/ycli1995/hdf5r.Extra"
	cran = "hdf5r.Extra" 

	version("0.0.5", md5="2dcfa159661bd152e6085113e92453f6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-hdf5r@1.3.8:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-easy-utils", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
