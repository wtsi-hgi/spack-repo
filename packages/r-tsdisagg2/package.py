# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdisagg2(RPackage):
	"""Time Series Disaggregation

	Disaggregates low frequency time series data to higher frequency series. Implements the following methods for temporal disaggregation: Boot, Feibes and Lisman (1967) <DOI:10.2307/2985238>, Chow and Lin (1971) <DOI:10.2307/1928739>, Fernandez (1981) <DOI:10.2307/1924371> and Litterman (1983) <DOI:10.2307/1391858>.
	"""
	
	cran = "tsdisagg2" 

	version("0.1.0", md5="f950630d99a50c5c2974d071bdba0c5b", url="https://cran.r-project.org/src/contrib/tsdisagg2_0.1.0.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
