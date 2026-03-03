# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtrackr(RPackage):
	"""Manipulate and Play 'ProTracker' Modules

	'ProTracker' is a popular music tracker to sequence
    music on a Commodore Amiga machine. This package offers the
    opportunity to import, export, manipulate and play 'ProTracker'
    module files. Even though the file format could be considered
    archaic, it still remains popular to this date. This package
    intends to contribute to this popularity and therewith
    keeping the legacy of 'ProTracker' and the Commodore Amiga
    alive.
	"""
	
	homepage = "https://pepijn-devries.github.io/ProTrackR/"
	cran = "ProTrackR" 

	version("0.4.3", md5="d75ce360c345ecd22907d9d9f0d89ec0")

	depends_on("r-audio", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-tuner@1:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
