# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynamaedes(RPackage):
	"""A Unified Mechanistic Model for the Population Dynamics of
Invasive Aedes Mosquitoes

	Generalised model for population dynamics of invasive Aedes mosquitoes. Rationale and model structure are described here: Da Re et al. (2021) <doi:10.1016/j.ecoinf.2020.101180> and Da Re et al. (2022) <doi:10.1101/2021.12.21.473628>.
	"""
	
	homepage = "https://mattmar.github.io/dynamAedes/"
	cran = "dynamAedes" 

	version("2.2.9", md5="5c0832a3a1d8211cbd8c7e5de721388b")
	version("2.2.8", md5="3dad4d6835040959bc3a61c1191b5546")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
