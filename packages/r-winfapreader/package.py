# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWinfapreader(RPackage):
	"""Interact with Peak Flow Data in the United Kingdom

	Obtain information on peak flow data from the National River Flow Archive (NRFA) in the United Kingdom, either from the Peak Flow Dataset files <https://nrfa.ceh.ac.uk/peak-flow-dataset> once these have been downloaded to the user's computer or using the NRFA's API. These files are in a format suitable for direct use in the 'WINFAP' software, hence the name of the package. 
	"""
	
	homepage = "https://ilapros.github.io/winfapReader/"
	cran = "winfapReader" 

	version("0.1-5", md5="e919ff5803904a275727a28551da7314")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
