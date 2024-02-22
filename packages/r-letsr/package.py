# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLetsr(RPackage):
	"""Data Handling and Analysis in Macroecology

	Handling, processing, and analyzing geographic
    data on species' distributions and environmental variables. 
    Read Vilela & Villalobos (2015) <doi:10.1111/2041-210X.12401> for details.
	"""
	
	homepage = "https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.12401"
	cran = "letsR" 

	version("5.0", md5="291afe2230afa3aa6a5b0a2c11a4390a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
