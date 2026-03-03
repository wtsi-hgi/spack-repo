# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalendrio(RPackage):
	"""'calendR' Fork with Additional Features (Backwards Compatible)

	Fork of 'calendR' R package to generate ready to print
  calendars with 'ggplot2' (see <https://r-coder.com/calendar-plot-r/>)
  with additional features (backwards compatible).
  'calendRio' provides a 'calendR()' function that serves as a drop-in
  replacement for the upstream version but allows for additional
  parameters unlocking extra functionality.
	"""
	
	cran = "calendRio" 

	version("0.2.0", md5="dcc314061b3f75396e345503c29f9571")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-gggibbous", type=("build", "run"))
	depends_on("r-ggimage", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-suncalc", type=("build", "run"))
