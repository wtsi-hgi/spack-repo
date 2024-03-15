# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdf5array(RPackage):
	"""HDF5 backend for DelayedArray objects.

	Implements the HDF5Array and TENxMatrix classes, 2 convenient and
	memory-efficient array-like containers for on-disk representation of
	HDF5 datasets. HDF5Array is for datasets that use the conventional (i.e.
	dense) HDF5 representation. TENxMatrix is for datasets that use the
	HDF5-based sparse matrix representation from 10x Genomics (e.g. the 1.3
	Million Brain Cell Dataset). Both containers being DelayedArray
	extensions, they support all operations supported by DelayedArray
	objects. These operations can be either delayed or block-processed."""

	bioc = "HDF5Array"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HDF5Array_1.30.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HDF5Array/HDF5Array_1.30.1.tar.gz"]

	version("1.30.1", md5="880ca20592c69a77a31650298a9c67bf")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
	depends_on("r-rhdf5@2.31.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rhdf5filters", type=("build", "run"))
	depends_on("r-biocgenerics@0.31.5:", type=("build", "run"))
	depends_on("r-s4vectors@0.27.13:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4arrays@1.1.1:", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
