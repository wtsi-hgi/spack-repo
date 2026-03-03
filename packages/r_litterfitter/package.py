# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLitterfitter(RPackage):
	"""Fit a Collection of Curves to Single Cohort Decomposition Data

	There is a long tradition of studying the flux of carbon from the biosphere to the atmosphere by following a particular cohort of litter (wood, leaves, roots, or other organic material) through time.  The resulting data are mass remaining and time. A variety of functional forms may be used to fit the resulting data. Some work better empirically. Some are better connected to a process-based understanding.  Some have a small number of free parameters; others have more. This package matches decomposition data to a family of these curves using likelihood--based fitting. This package is based on published research by Cornwell & Weedon (2013) <doi:10.1111/2041-210X.12138>.
	"""
	
	homepage = "https://github.com/traitecoevo/litterfitter/issues"
	cran = "litterfitter" 

	version("0.1.3", md5="dc9f35c4c5848a4198323b3fa90c9e3e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
