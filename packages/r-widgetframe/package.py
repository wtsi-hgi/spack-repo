# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWidgetframe(RPackage):
	"""'Htmlwidgets' in Responsive 'iframes'

	Provides two functions 'frameableWidget()', and 'frameWidget()'.
  The 'frameableWidget()' is used to add extra code to a 'htmlwidget' which
  allows is to be rendered correctly inside a responsive 'iframe'.
  The 'frameWidget()' is a 'htmlwidget' which displays content of another 'htmlwidget'
  inside a responsive 'iframe'.
  These functions allow for easier embedding of 'htmlwidgets' in content management systems
  such as 'wordpress', 'blogger' etc.
  They also allow for separation of widget content from main HTML content where
  CSS of the main HTML could interfere with the widget.
	"""
	
	homepage = "https://github.com/bhaskarvk/widgetframe"
	cran = "widgetframe" 

	version("0.3.1", md5="5676463337ddfaffe9c3d53c44061bc0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
