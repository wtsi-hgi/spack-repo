# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeSlots(RPackage):
	"""Display Data in a Weekly Calendar View

	Generate weekly timetables as a ggplot2 layer. Add
    informative timeslots with elements such as title, key-value pairs, or
    colour to reveal trends.
	"""
	
	homepage = "https://bitbucket.org/annalectnz/time.slots"
	cran = "time.slots" 

	version("0.2.0", md5="2ad8e20bbd920c27376c2d4e8e39db6d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
