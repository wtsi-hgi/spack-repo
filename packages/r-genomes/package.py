# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomes(RPackage):
	"""Genome sequencing project metadata

	Download genome and assembly reports from NCBI
	"""
	
	bioc = "genomes"

	version("3.38.0", commit="c404ec9f6e885d500a7c4f79b5dbcda7162dbbac")
	version("3.32.0", commit="9bcaa80ba14957a6e6289480ab8547afa4967ea7")

	depends_on("r-readr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
