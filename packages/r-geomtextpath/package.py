# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomtextpath(RPackage):
	"""Curved Text in 'ggplot2'

	A 'ggplot2' extension that allows text to follow curved paths.
    Curved text makes it easier to directly label paths or neatly annotate in 
    polar co-ordinates.
	"""
	
	homepage = "https://allancameron.github.io/geomtextpath/"
	cran = "geomtextpath" 

	version("0.1.3", md5="4018c5bba964c6f0d35fb69596c30cfc")
	version("0.1.1", md5="4f8ffb3dd993d18a661a9df781fadcd1")

	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-systemfonts", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-textshaping", type=("build", "run"))
