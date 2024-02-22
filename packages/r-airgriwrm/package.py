# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirgriwrm(RPackage):
	"""'airGR' Integrated Water Resource Management

	Semi-distributed Precipitation-Runoff Modelling based on
    'airGR' package models integrating human infrastructures and their
    managements.
	"""
	
	homepage = "https://airgriwrm.g-eau.fr/"
	cran = "airGRiwrm" 

	version("0.6.2", md5="d32a631b551567a15453980e2233b060")

	depends_on("r-airgr@1.7:", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
