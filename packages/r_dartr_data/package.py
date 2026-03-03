# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDartrData(RPackage):
	"""Auxiliary Data Package for Our Main Package 'dartR'

	Data package for 'dartR'. Provides data sets to run examples in 'dartR'. This was necessary due to the size limit imposed by 'CRAN'. The data in 'dartR.data' is needed to run the examples provided in the 'dartR' functions. All available data sets are either based on actual data (but reduced in size) and/or simulated data sets to allow the fast execution of examples and demonstration of the functions. 
	"""
	
	homepage = "https://github.com/green-striped-gecko/dartR.data"
	cran = "dartR.data" 

	version("1.0.2", md5="6e569e2271eaaea536ffc820b5f1e428")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-adegenet@2:", type=("build", "run"))
