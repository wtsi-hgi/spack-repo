# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwiper(RPackage):
	"""Carousels using the 'JavaScript' Library 'Swiper'

	Create carousels using the 'JavaScript' library 'Swiper' and
    the package 'htmlwidgets'. The carousels can be displayed in the
    'RStudio' viewer pane, in 'Shiny' applications and in 'R markdown'
    documents. The package also provides a 'RStudio' addin allowing to 
    choose image files and to display them in the viewer pane.
	"""
	
	homepage = "https://github.com/stla/swipeR"
	cran = "swipeR" 

	version("1.1.0", md5="de2e6ed8c746596b030cbb4e1aaa96ae")

	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rchoicedialogs", type=("build", "run"))
