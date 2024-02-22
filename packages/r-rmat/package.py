# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmat(RPackage):
	"""Random Matrix Analysis Toolkit

	Simulate random matrices and ensembles and compute their eigenvalue spectra and dispersions.
	"""
	
	cran = "RMAT" 

	version("0.2.0", md5="a10e5681dc85fd9ea78e5fbfe23981cc")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
