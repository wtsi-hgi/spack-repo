# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTemperatureresponse(RPackage):
	"""Temperature Response

	Fits temperature response models to rate measurements taken at different temperatures. Etienne Low-Decarie,Tobias G. Boatman, Noah Bennett,Will Passfield,Antonio Gavalas-Olea,Philipp Siegel, Richard J. Geider (2017) <doi:10.1002/ece3.3576> .
	"""
	
	homepage = "https://github.com/low-decarie/temperatureresponse"
	cran = "temperatureresponse" 

	version("0.2", md5="702f0cd7bba3ff8cb071effd1c1383f5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-aiccmodavg", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
