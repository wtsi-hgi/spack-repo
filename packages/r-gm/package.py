# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGm(RPackage):
	"""Generate Music Easily and Show Them Anywhere

	Provides a simple and intuitive high-level language, with which
    you can create music easily. Takes care of all the dirty technical
    details in converting your music to musical scores and audio files.
    Works in 'R Markdown' documents <https://rmarkdown.rstudio.com/>,
    R 'Jupyter Notebooks' <https://jupyter.org/>, and 'RStudio'
    <https://www.rstudio.com/>, so you can embed generated music
    anywhere. Internally, uses 'MusicXML' <https://www.musicxml.com/> to
    represent musical scores, and 'MuseScore' <https://musescore.org/> to
    convert 'MusicXML'.
	"""
	
	homepage = "https://github.com/flujoo/gm"
	cran = "gm" 

	version("1.0.2", md5="2020139512492d5134016a4533082220")

	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
