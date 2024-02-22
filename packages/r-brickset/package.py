# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrickset(RPackage):
	"""Interface with the Brickset API for Getting Data About LEGO Sets

	Interface with the 'Brickset' API
    <https://brickset.com/article/52664/api-version-3-documentation> for
    getting data about LEGO sets. Data sets that
    can be used for teaching and learning without the need of a 'Brickset'
    account and API key are also included. Includes all LEGO since through
    the end of 2023.
	"""
	
	homepage = "https://github.com/jbryer/brickset"
	cran = "brickset" 

	version("2024.0.0", md5="55a7694909832d411e068ac9e2bd791a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-piggyback", type=("build", "run"))
