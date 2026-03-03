# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGemlog(RPackage):
	"""File Conversion for 'Gem Infrasound Logger'

	Reads data files from the 'Gem infrasound logger' for analysis and converts to segy format (which is convenient for reading with traditional seismic analysis software). The Gem infrasound logger is a low-cost, lightweight, low-power instrument for recording infrasound in field campaigns; email the maintainer for more information.
	"""
	
	cran = "gemlog" 

	version("0.41", md5="023cecbdb0a03f27ca6a68908f334104")

	depends_on("r-signal", type=("build", "run"))
