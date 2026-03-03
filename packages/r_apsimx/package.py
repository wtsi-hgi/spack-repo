# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApsimx(RPackage):
	"""Inspect, Read, Edit and Run 'APSIM' "Next Generation" and
'APSIM' Classic

	The functions in this package inspect, read, edit and run files for 'APSIM' "Next Generation" ('JSON')
             and 'APSIM' "Classic" ('XML'). The files with an 'apsim' extension correspond to
	     'APSIM' Classic (7.x) - Windows only - and the ones with an 'apsimx' extension correspond to 'APSIM' "Next Generation".
	     For more information about 'APSIM' see (<https://www.apsim.info/>) and for 'APSIM'
	     next generation (<https://apsimnextgeneration.netlify.app/>). 
	"""
	
	cran = "apsimx" 

	version("2.6.2", md5="e4c78dbde7eb9ba67e5dbfc80fb4f68b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
