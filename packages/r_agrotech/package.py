# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgrotech(RPackage):
	"""Data Analysis of Pesticide Application Technology

	In total it has 7 functions, three for calculating machine calibration, which determine application rate (L/ha), nozzle flow (L/min) and amount of product (L or kg) to be added. to the tank with each sprayer filling. Two functions for graphs of the flow distribution of the nozzles (L/min) in the application bar and, of the temporal variability of the meteorological conditions (air temperature, relative humidity of the air and wind speed). Two functions to determine the spray deposit (uL/cm2), through the methodology called spectrophotometry, with the aid of bright blue (Palladini, L.A., Raetano, C.G., Velini, E.D. (2005), <doi:10.1590/S0103-90162005000500005>) or metallic markers (Chaim, A., Castro, V.L.S.S., Correles, F.M., Galvão, J.A.H., Cabral, O.M.R., Nicolella, G. (1999), <doi:10.1590/S0100-204X1999000500003>). The package supports the analysis and representation of information, using a single free software that meets the most diverse areas of activity in application technology.
	"""
	
	cran = "AgroTech" 

	version("1.0.2", md5="e9df0519789cf1c39d5091774874e9f1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
