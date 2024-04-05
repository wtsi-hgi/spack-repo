# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAndromeda(RPackage):
	"""Asynchronous Disk-Based Representation of Massive Data

	Storing very large data objects on a local drive, while still making it possible to manipulate the data in an efficient manner.
	"""
	
	homepage = "https://github.com/OHDSI/Andromeda"
	cran = "Andromeda" 

	version("0.6.6", md5="ba90c6ef2b4541816c31cbaa66551fd2")
	version("0.6.5", md5="120903424410e1b092410e8efb169b9e")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
