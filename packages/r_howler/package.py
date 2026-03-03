# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHowler(RPackage):
	"""'Shiny' Extension of 'howler.js'

	Audio interactivity within 'shiny' applications using 'howler.js'. Enables the
    status of the audio player to be sent from the UI to the server, and events such as
    playing and pausing the audio can be triggered from the server.
	"""
	
	homepage = "https://github.com/ashbaldry/howler"
	cran = "howler" 

	version("0.2.1", md5="350ed3dce0f6b4b725b5ab3bde7716c6")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
