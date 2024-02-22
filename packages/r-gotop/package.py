# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGotop(RPackage):
	"""Scroll Back to Top Icon in 'rmarkdown' and 'shiny'

	Add a scroll back to top 'Font Awesome' icon 
    <https://fontawesome.com/> in 'rmarkdown' documents and 'shiny'
    apps thanks to 'jQuery GoTop' <https://scottdorman.blog/jquery-gotop/>.
	"""
	
	homepage = "https://felixluginbuhl.com/gotop"
	cran = "gotop" 

	version("0.1.2", md5="26c1e7fc967dea8be4114fd59a446571")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
