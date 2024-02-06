# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXaringanthemer(RPackage):
	"""Custom 'xaringan' CSS Themes

	Create beautifully color-coordinated and customized themes
    for your 'xaringan' slides, without writing any CSS. Complete your
    slide theme with 'ggplot2' themes that match the font and colors used
    in your slides.  Customized styles can be created directly in your
    slides' 'R Markdown' source file or in a separate external script.
	"""
	
	homepage = "https://pkg.garrickadenbuie.com/xaringanthemer/"
	cran = "xaringanthemer" 

	version("0.4.2", md5="05934dccc04d5029a3a92ad56bd63b45")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
