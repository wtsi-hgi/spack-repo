# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodelink(RPackage):
	"""Manipulation of Codelink microarray data

	This package facilitates reading, preprocessing and manipulating Codelink microarray data. The raw data must be exported as text file using the Codelink software.
	"""
	
	homepage = "https://github.com/ddiez/codelink"
	bioc = "codelink"

	version("1.76.0", commit="bfa3e6d8456ddca6264b23d31d86cb42523fa6b8")
	version("1.70.0", commit="2bef0c7b15f5af5a390c9070236c87bcc9643bdd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics@0.3.2:", type=("build", "run"))
	depends_on("r-biobase@2.17.8:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
