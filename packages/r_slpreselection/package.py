# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlpreselection(RPackage):
	"""Presidential Election Data of "Sri Lanka" from 1982 to 2015

	Presidential Election data of "Sri Lanka"" is stored in Pdf
    files, through Pdf scraping they are converted into data-frames and
    stored in this R package.
	"""
	
	homepage = "https://github.com/Amalan-ConStat/SLPresElection"
	cran = "SLPresElection" 

	version("1.0.0", md5="1ad8acc0f4d582e4169d3a77024f0439")

	depends_on("r@4:", type=("build", "run"))
