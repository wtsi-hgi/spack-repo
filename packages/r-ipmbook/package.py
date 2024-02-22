# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpmbook(RPackage):
	"""Functions and Data for the Book 'Integrated Population Models'

	Provides functions and data sets to accompany the  book 'Integrated Population Models: Theory and Ecological Applications with R and JAGS' by Michael Schaub and Marc Kéry (ISBN: 9780128205648).
	"""
	
	homepage = "https://www.vogelwarte.ch/de/projekte/publikationen/ipm/"
	cran = "IPMbook" 

	version("0.1.5", md5="5e7a4e1fd04bcf77b926b33286953c85")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
