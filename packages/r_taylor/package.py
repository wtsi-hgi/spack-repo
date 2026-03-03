# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaylor(RPackage):
	"""Lyrics and Song Data for Taylor Swift's Discography

	A comprehensive resource for data on Taylor Swift songs. Data is
    included for all officially released studio albums, extended plays (EPs),
    and individual singles are included. Data comes from
    'Genius' (lyrics) and 'Spotify' (song characteristics). Additional functions
    are included for easily creating data visualizations with color palettes
    inspired by Taylor Swift's album covers.
	"""
	
	homepage = "https://taylor.wjakethompson.com"
	cran = "taylor" 

	version("3.0.0", md5="48e998fc8c53136f55d43fa192edc1ac")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
