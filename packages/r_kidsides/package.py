# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKidsides(RPackage):
	"""Download, Cache, and Connect to KidSIDES

	Caches and then connects to a 'sqlite' database containing half a million pediatric drug safety signals. 
    The database is part of a family of resources catalogued at <https://nsides.io>. The database
    contains 17 tables where the description table provides a map between the fields the field's details. 
    The database was created by Nicholas Giangreco during his PhD thesis which you can read in Giangreco (2022) <doi:10.7916/d8-5d9b-6738>. 
    The observations are from the Food and Drug Administration's Adverse Event Reporting System. Generalized additive models estimated
    drug effects across child development stages for the occurrence of an adverse event when exposed to a drug compared to other drugs.
    Read more at the methods detailed in Giangreco (2022) <doi:10.1016/j.medj.2022.06.001>. 
	"""
	
	homepage = "https://github.com/ngiangre/kidsides"
	cran = "kidsides" 

	version("0.5.0", md5="786c0226295c2c6bd02097d0f8f92ccb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
