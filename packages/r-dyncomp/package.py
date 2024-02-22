# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyncomp(RPackage):
	"""Complexity of Short and Coarse-Grained Time Series

	While there are many well-established measures for identifying critical fluctuations and phase transitions, these measures only work with many points of measurement and thus are unreliable when studying short and coarse-grained time series. This package provides a measure for complexity in a time series that does not rely on long time series (Kaiser (2017), <doi:10.17605/OSF.IO/GWTKX>). 
	"""
	
	cran = "dyncomp" 

	version("0.0.2-1", md5="7e8622d34003a07a071845d28302369f")

	depends_on("r-zoo", type=("build", "run"))
