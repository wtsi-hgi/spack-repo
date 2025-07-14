# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwascatdata(RPackage):
	"""A text file in cloud with March 30 2021 snapshot of EBI/EMBL GWAS catalog

	This package manages a text file in cloud with March 30 2021 snapshot of EBI/EMBL GWAS catalog.This simplifies access to a snapshot of EBI GWASCAT.  More current images can be obtained using the gwascat package.
	"""
	
	bioc = "gwascatData"

	version("0.99.6", commit="cf9495ac3a7fa6b14c56c4132984a4b8c4b86f7c")
	version("0.99.6", commit="cf9495ac3a7fa6b14c56c4132984a4b8c4b86f7c")

	depends_on("r-data-table", type=("build", "run"))

