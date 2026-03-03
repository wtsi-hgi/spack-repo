# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXaringanextra(RPackage):
	"""Extras and Extensions for 'xaringan' Slides

	Extras and extensions for 'xaringan' slides. Navigate your
    slides with tile view. Make your slides editable, live! Announce slide
    changes with subtle tones. Animate slide transitions with
    'animate.css'. Add tabbed panels to slides with 'panelset'. Use the
    'Tachyons CSS' utility toolkit for rapid slide development. Scribble
    on your slides. Add a copy button to your code chunks with
    'clipboard'. Add a logo or top or bottom banner to every slide.
    Broadcast slides to stay in sync with remote viewers. Include yourself
    in your slides with 'webcam'.  Plus a whole lot more!
	"""
	
	homepage = "https://pkg.garrickadenbuie.com/xaringanExtra/"
	cran = "xaringanExtra" 

	version("0.7.0", md5="00f548d76eb82ba23f14f645b4918bdb")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
