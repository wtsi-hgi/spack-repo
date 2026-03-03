# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdeamdb(RPackage):
	"""Easy Manipulation of IDEAM's Climatological Data

	Time series plain text conversion and data visualization. It allows
    to transform IDEAM (Instituto de Hidrologia, Meteorologia y Estudios Ambientales)
    daily series from plain text to CSV files or data frames in R. Additionally,
    it is possible to obtain exploratory graphs from times series. IDEAM’s data
    is freely delivered under formal request through the official web page
    <http://www.ideam.gov.co/solicitud-de-informacion>.
	"""
	
	cran = "ideamdb" 

	version("0.0.9", md5="4788715b824cc7cde29718c5eaecce62")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
