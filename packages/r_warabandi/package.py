# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWarabandi(RPackage):
	"""Roster Generation of Turn for Weekdays:'warabandi'

	It generates the roster of turn for an outlet which is flowing 
        (water) 24X7 or 168 hours towards the area under command or agricutural 
        area (to be irrigated). The area under command is differentially owned 
        by different individual farmers. The Outlet runs for free of cost to 
        irrigate the area under command 24X7.
        So, flow time of the outlet has to be divided based on an area owned by 
        an individual farmer and the location of his land or farm. This roster 
        is known as 'warabandi' and its generation in agriculture practices is a 
        very tedious task. Calculations of time in microseconds are more 
        error-prone, especially whenever it is performed by hands. That division
        of flow time for an individual farmer can be calculated by 'warabandi'. 
        However, it generates a full publishable report for an outlet and all the 
        farmers who have farms subjected to be irrigated. 
        It reduces error risk and makes a more reproducible roster. For more 
        details about warabandi system you can found elsewhere in 
        Bandaragoda DJ(1995) <https://publications.iwmi.org/pdf/H_17571i.pdf>.
	"""
	
	cran = "warabandi" 

	version("0.1.0", md5="2865a542d3334eedfb7549c10360aa1a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readtext", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
