# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIspdata(RPackage):
	"""Access Data from the Public Security Institute of the State of
Rio De Janeiro

	Allows access to data from the Rio de Janeiro Public Security Institute (ISP), such as criminal statistics, data on gun seizures and femicide. The package also contains the spatial data of Pacifying Police Units (UPPs) and Integrated Public Safety Regions, Areas and Circumscriptions. 
	"""
	
	cran = "ispdata" 

	version("1.1.2", md5="a8ccc7fc797a14edb5fcd1a9fe8b0fe5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
