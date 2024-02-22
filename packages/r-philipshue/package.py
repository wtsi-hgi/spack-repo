# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhilipshue(RPackage):
	"""R Interface to the Philips Hue API

	Control Philips Hue smart lighting. Use this package to
    connect to a Hue bridge on your local network (remote authentication
    not yet supported) and control your smart lights through the Philips
    Hue API. All API V1 endpoints are supported. See API documentation at
    <https://developers.meethue.com/>.
	"""
	
	homepage = "https://fascinatingfingers.gitlab.io/philipshue"
	cran = "PhilipsHue" 

	version("1.0.0", md5="6b470321b5b48a56c82e061ff83b261f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
