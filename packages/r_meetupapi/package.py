# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeetupapi(RPackage):
	"""Access 'Meetup' API

	Allows management of 'Meetup' groups via the <https:www.meetup.com/meetup_api/>.
    Provided are a set of functions that enable fetching information of joined meetups, attendance,
    and members. This package requires the use of an API key.
	"""
	
	homepage = "https://github.com/zacdav/meetupapi"
	cran = "meetupapi" 

	version("0.1.0", md5="65cb271dee1754bd0172e48de963aaa5")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
