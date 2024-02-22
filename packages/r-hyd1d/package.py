# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyd1d(RPackage):
	"""1d Water Level Interpolation along the Rivers Elbe and Rhine

	An S4 class and several functions which utilize internally stored
    datasets and gauging data enable 1d water level interpolation. The S4 class
    (WaterLevelDataFrame) structures the computation and visualisation
    of 1d water level information along the German federal waterways Elbe and
    Rhine. 'hyd1d' delivers 1d water level data - extracted from the 'FLYS'
    database - and validated gauging data - extracted from the hydrological
    database 'HyDaBa' - package-internally. For computations near real time
    gauging data are queried externally from the 'PEGELONLINE REST API' 
    <https://pegelonline.wsv.de/webservice/dokuRestapi>.
	"""
	
	homepage = "https://hyd1d.bafg.de"
	cran = "hyd1d" 

	version("0.5.1", md5="eb4f4584f890e3d543d8e8ea1ad93d01")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
