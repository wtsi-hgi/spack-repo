# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProjectmanagement(RPackage):
	"""Management of Deterministic and Stochastic Projects

	Management problems of deterministic and stochastic projects. It obtains the duration of a project and the appropriate slack for each activity in a deterministic context. In addition it obtains a schedule of activities' time (Castro, Gómez & Tejada (2007) <doi:10.1016/j.orl.2007.01.003>). It also allows the management of resources. When the project is done, and the actual duration for each activity is known, then it can know how long the project is delayed and make a fair delivery of the delay between each activity (Bergantiños, Valencia-Toledo & Vidal-Puga (2018) <doi:10.1016/j.dam.2017.08.012>). In a stochastic context it can estimate the average duration of the project and plot the density of this duration, as well as, the density of the early and last times of the chosen activities. As in the deterministic case, it can make a distribution of the delay generated by observing the project already carried out.
	"""
	
	cran = "ProjectManagement" 

	version("1.5.2", md5="369415c63fab9fb78f571514d8ad2d1d")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-kappalab", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
