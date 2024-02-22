# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcal(RPackage):
	"""'iCalendar' Parsing

	A simple wrapper around the 'ical.js' library executing 
    'Javascript' code via 'V8' (the 'Javascript' engine driving the 'Chrome' 
    browser and 'Node.js' and accessible via the 'V8' R package). 
    This package enables users to parse 'iCalendar' files ('.ics', '.ifb', 
    '.iCal', '.iFBf') into lists and 'data.frames' to ultimately do statistics
    on events, meetings, schedules, birthdays, and the like.
	"""
	
	cran = "ical" 

	version("0.1.6", md5="1a7f6bc27d0558ff4eb5ff8e4d91fcce")

	depends_on("r-v8@1.5:", type=("build", "run"))
