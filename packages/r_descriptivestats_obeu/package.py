# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescriptivestatsObeu(RPackage):
	"""Descriptive Statistics 'OpenBudgets.eu'

	Estimate and return the needed parameters for visualizations designed for 'OpenBudgets.eu' <http://openbudgets.eu/> datasets. Calculate descriptive statistical measures in budget data of municipalities across Europe, according to the 'OpenBudgets.eu' data model. There are functions for measuring central tendency and dispersion of amount variables along with their distributions and correlations and the frequencies of categorical variables for a given dataset. Also, can be used generally to other datasets, to extract visualization parameters, convert them to 'JSON' format and use them as input in a different graphical interface. 
	"""
	
	homepage = "https://github.com/okgreece/DescriptiveStats.OBeu"
	cran = "DescriptiveStats.OBeu" 

	version("1.3.2", md5="7f23a7e343efd1c311ae1d8355bbecd5")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
