# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgreenplum(RPackage):
	"""Interface to 'Greenplum' Database

	
    Fully 'DBI'-compliant interface to 'Greenplum' <https://greenplum.org/>,
    an open-source parallel database. This is an extension of the 'RPostgres'
    package <https://github.com/r-dbi/RPostgres>.
	"""
	
	homepage = "https://github.com/mwillumz/RGreenplum"
	cran = "RGreenplum" 

	version("0.1.2", md5="f10ed6c209bd59bdd6a6566853201a0f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rpostgres", type=("build", "run"))
