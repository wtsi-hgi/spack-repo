# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntamapinteractive(RPackage):
	"""Interactive Add-on Functionality for 'intamap'

	The methods in this package adds to the functionality of  the 'intamap' package, such as bias correction and network optimization. Pebesma et al (2010) gives an overview of the methods behind and possible usage <doi:10.1016/j.cageo.2010.03.019>.
	"""
	
	cran = "intamapInteractive" 

	version("1.2-6", md5="ab50d35c10ff9a0b6064082cfbf0a88c")

	depends_on("r-intamap", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-automap", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spcosa", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
