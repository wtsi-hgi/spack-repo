# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRghanacensus(RPackage):
	"""2021 Ghana Population and Housing Census Results as Data Frames

	Datasets from the 2021 Ghana Population and Housing Census Results. Users can access results as 'tidyverse' and 'sf'-Ready Data Frames.    The data in this package is scraped from pdf reports released by the Ghana Statistical Service website <https://census2021.statsghana.gov.gh/> . The package currently only contains datasets from the literacy and education reports. Namely, school attendance data for respondents aged 3 years and above.
	"""
	
	homepage = "https://github.com/ktemadarko/rGhanaCensus"
	cran = "rGhanaCensus" 

	version("0.1.0", md5="1cc75c6dcb4084edf98b006d0f6e8668")

	depends_on("r@3.5:", type=("build", "run"))
