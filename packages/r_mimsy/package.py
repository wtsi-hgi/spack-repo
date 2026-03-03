# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMimsy(RPackage):
	"""Calculate MIMS Dissolved Gas Concentrations Without Getting a
Headache

	Calculate dissolved gas concentrations from raw MIMS 
	(Membrane Inlet Mass Spectrometer) signal data. Use mimsy() on 
	a formatted CSV file to return dissolved gas concentrations 
	(mg and microMole) of N2, O2, Ar based on 
	gas solubility at temperature, pressure, and salinity. See references 
	Benson and Krause (1984), Garcia and Gordon (1992), Stull (1947), 
	and Hamme and Emerson (2004) for more information. Easily save the 
	output to a nicely-formatted multi-tab 'Excel' workbook with mimsy.save(). 
	Supports dual-temperature standard calibration for dual-bath MIMS setups.
	"""
	
	homepage = "https://github.com/michelleckelly/mimsy"
	cran = "mimsy" 

	version("0.6.4", md5="e5f954566fbb8c5791687539a77f9f5e")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
