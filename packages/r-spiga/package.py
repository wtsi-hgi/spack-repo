# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpiga(RPackage):
	"""Compute SPI Index using the Methods Genetic Algorithm and
Maximum Likelihood

	Calculate the Standardized Precipitation Index (SPI) for monitoring drought, using Artificial Intelligence techniques (SPIGA) and traditional numerical technique Maximum Likelihood (SPIML).  For more information see: http://drought.unl.edu/monitoringtools/downloadablespiprogram.aspx.
	"""
	
	cran = "SPIGA" 

	version("1.0.0", md5="fd583b668b188878506117a267fe7ae1")

	depends_on("r-ga", type=("build", "run"))
