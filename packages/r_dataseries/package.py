# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataseries(RPackage):
	"""Switzerland's Data Series in One Place

	Download and import time series from <http://www.dataseries.org>, a comprehensive and up-to-date collection of open data from Switzerland.
	"""
	
	homepage = "http://www.dataseries.org"
	cran = "dataseries" 

	version("0.2.0", md5="79eb12da3581a880777aace601ffbb9d")

