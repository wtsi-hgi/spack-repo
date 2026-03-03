# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalendar(RPackage):
	"""Create, Read, Write, and Work with 'iCalander' Files, Calendars
and Scheduling Data

	Provides function to create, read, write, and work with 'iCalander' files
  (which typically have '.ics' or '.ical' extensions), and the scheduling data,
  calendars and timelines of people, organisations and other entities that they represent.
  'iCalendar' is an open standard for
  exchanging calendar and scheduling information between users and computers, 
  described at <https://icalendar.org/>.
	"""
	
	cran = "calendar" 

	version("0.0.1", md5="095781e80c88e870a429f2d0b922ef75")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
