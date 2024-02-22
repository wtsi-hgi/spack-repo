# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKehra(RPackage):
	"""Collect, Assemble and Model Air Pollution, Weather and Health
Data

	Collection of utility functions used in the KEHRA project (see http://www.brunel.ac.uk/ife/britishcouncil). It refers to the multidimensional analysis of air pollution, weather and health data.
	"""
	
	homepage = "https://github.com/kehraProject/r_kehra"
	cran = "kehra" 

	version("0.1", md5="5799e1c21f576a96bcbe50448a57f8e8")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
