# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimelinegraphics(RPackage):
	"""HTML with Horizontal Strips Symbolizing Events in a Person's
Life

	Produce an HTML page containing horizontal strips that symbolize events in a person's lsife. Since this is entirely a visualization, the image <https://barryzee.github.io/henry-timeline/henry.html> will show the basic use to show a timeline of events. The image <https://barryzee.github.io/vermeer/cssOverlay.html> shows how to correlate two timelines of events. A brief description is available at <https://barryzee.github.io/timeLineGraphics_manuscript/golden_age.html>.
	"""
	
	cran = "timeLineGraphics" 

	version("1.0", md5="828152373c9207952c034e3e5858593b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-berryfunctions", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
