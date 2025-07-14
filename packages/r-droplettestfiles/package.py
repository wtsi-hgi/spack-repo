# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDroplettestfiles(RPackage):
	"""Test Files for Single-Cell Droplet Utilities

	Assorted files generated from droplet-based single-cell protocols, to be used for testing functions in DropletUtils. Primarily intended for storing files that directly come out of processing pipelines like 10X Genomics' CellRanger software, prior to the formation of a SingleCellExperiment object. Unlike other packages, this is not designed to provide objects that are immediately ready for analysis.
	"""
	
	bioc = "DropletTestFiles"

	version("1.18.0", commit="1a3668cab6e275407730d73ad2d62435e60774ef")
	version("1.12.0", commit="2ca3a3890371bfe5231f115fcc015c05454a71e6")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

