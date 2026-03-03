# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHospitalnetwork(RPackage):
	"""Building Networks of Hospitals Through Patients Transfers

	Set of tools to help interested researchers to build hospital networks 
  from data on hospitalized patients transferred between hospitals. Methods provided 
  have been used in Donker T, Wallinga J, Grundmann H. (2010) <doi:10.1371/journal.pcbi.1000715>, 
  and Nekkab N, Crépey P, Astagneau P, Opatowski L, Temime L. (2020) <doi:10.1038/s41598-020-71212-6>.
	"""
	
	homepage = "https://pascalcrepey.github.io/HospitalNetwork/"
	cran = "HospitalNetwork" 

	version("0.9.3", md5="368c23b07a5bef684ea5a09a2c3d0b16")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
