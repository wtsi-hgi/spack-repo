# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsn2(RPackage):
	"""Spatial Modeling on Stream Networks

	Spatial statistical modeling and prediction for data on stream networks, including models based on in-stream distance (Ver Hoef, J.M. and Peterson, E.E., (2010) <DOI:10.1198/jasa.2009.ap08248>.) Models are created using moving average constructions. Spatial linear models, including explanatory variables, can be fit with (restricted) maximum likelihood.  Mapping and other graphical functions are included. 
	"""
	
	homepage = "https://usepa.github.io/SSN2/"
	cran = "SSN2" 

	version("0.1.1", md5="bceb7f5d47771a64722a18a8d1786681", url="https://cran.r-project.org/src/contrib/SSN2_0.1.1.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-spmodel", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
