# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVideo(RPackage):
	"""'Shiny' Extension of 'video.js'

	Video interactivity within 'shiny' applications using 'video.js'. Enables
    the status of the video to be sent from the UI to the server, and allows events
    such as playing and pausing the video to be triggered from the server.
	"""
	
	homepage = "https://github.com/ashbaldry/video"
	cran = "video" 

	version("0.1.1", md5="725c3e97b473d0dea6253d2bbd60f9f9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
