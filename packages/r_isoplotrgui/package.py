# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsoplotrgui(RPackage):
	"""Web Interface to 'IsoplotR'

	Provides a graphical user interface to the 'IsoplotR' package for radiometric geochronology. The GUI runs in an internet browser and can either be used offline, or hosted on a server to provide online access to the 'IsoplotR' toolbox.
	"""
	
	homepage = "https://www.ucl.ac.uk/~ucfbpve/isoplotr/"
	cran = "IsoplotRgui" 

	version("6.1", md5="441d88710e9c730db5288519f8866296")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-isoplotr@6.1:", type=("build", "run"))
	depends_on("r-shinylight@1.1.2:", type=("build", "run"))
