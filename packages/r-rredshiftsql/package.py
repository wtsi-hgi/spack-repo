# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRredshiftsql(RPackage):
	"""R Interface to the 'Redshift' Database

	Superclasses 'PostgreSQL' connection to help enable full 'dplyr' functionality on 'Redshift'.
	"""
	
	cran = "RRedshiftSQL" 

	version("0.1.2", md5="6df219357b9a0bc8e842c19f9bd2a68b")

	depends_on("r-dbi@0.4.1:", type=("build", "run"))
	depends_on("r-rpostgresql@0.4.1:", type=("build", "run"))
