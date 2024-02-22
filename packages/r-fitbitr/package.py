# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitbitr(RPackage):
	"""Interface with the 'Fitbit' API

	Many 'Fitbit' users, and R-friendly 'Fitbit' users
    especially, have found themselves curious about their 'Fitbit' data.
    'Fitbit' aggregates a large amount of personal data, much of which is
    interesting for personal research and to satisfy curiosity, and is
    even potentially useful in medical settings. The goal of 'fitbitr' is
    to make interfacing with the 'Fitbit' API as streamlined as possible,
    to make it simple for R users of all backgrounds and comfort levels to
    analyze their 'Fitbit' data and do whatever they want with it!
    Currently, 'fitbitr' includes methods for pulling data on activity,
    sleep, and heart rate, but this list is likely to grow in the future
    as the package gains more traction and more requests for new methods
    to be implemented come in.  You can find details on the 'Fitbit' API
    at <https://dev.fitbit.com/build/reference/web-api/>.
	"""
	
	homepage = "https://github.com/mrkaye97/fitbitr"
	cran = "fitbitr" 

	version("0.3.0", md5="21bd1f760bbca91db0572f43c9b82843")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
