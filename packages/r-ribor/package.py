# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRibor(RPackage):
	"""An R Interface for Ribo Files

	The ribor package provides an R Interface for .ribo files. It provides functionality to read the .ribo file, which is of HDF5 format, and performs common analyses on its contents.
	"""
	
	bioc = "ribor"

	version("1.20.0", commit="834b57608c548d1b9577e0fbf9bcc74ee899d30f")
	version("1.14.0", commit="f006392b141d190c735460aaa6ed8f20bedd0b2c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
