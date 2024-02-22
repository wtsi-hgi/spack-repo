# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRh2(RPackage):
	"""DBI/RJDBC Interface to H2 Database

	DBI/RJDBC interface to h2 database. h2 version 1.3.175 is included.
	"""
	
	homepage = "https://github.com/dmkaplan2000/RH2.git"
	cran = "RH2" 

	version("0.2.4", md5="75921228b40823db4ff277e23812e9e9", url="https://cran.r-project.org/src/contrib/RH2_0.2.4.tar.gz")

	depends_on("r-chron", type=("build", "run"))
	depends_on("r-rjdbc", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))
