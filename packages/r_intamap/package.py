# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntamap(RPackage):
	"""Procedures for Automated Interpolation

	Geostatistical interpolation has traditionally been done by manually fitting a variogram and then interpolating. Here, we introduce classes and methods that can do this interpolation automatically. Pebesma et al (2010) gives an overview of the methods behind and possible usage <doi:10.1016/j.cageo.2010.03.019>.
	"""
	
	cran = "intamap" 

	version("1.5-7", md5="c88abf5021896a79bc2ae961ecb85d9c")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-sp@0.9.0:", type=("build", "run"))
	depends_on("r-gstat@0.9.36:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-automap", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
