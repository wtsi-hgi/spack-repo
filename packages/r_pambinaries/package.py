# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPambinaries(RPackage):
	"""Read and Process 'Pamguard' Binary Data

	Functions for easily reading and processing binary data files created by
    'Pamguard' (<https://www.pamguard.org/>). All functions for directly reading the
    binary data files are based on 'MATLAB' code written by Michael Oswald.
	"""
	
	cran = "PamBinaries" 

	version("1.8.0", md5="322686ad4b3f7bb4b61d2f8bf43f20f9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
