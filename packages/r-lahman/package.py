# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLahman(RPackage):
	"""Sean 'Lahman' Baseball Database

	Provides the tables from the 'Sean Lahman Baseball Database' as
    a set of R data.frames. It uses the data on pitching, hitting and fielding
    performance and other tables from 1871 through 2022, as recorded in the 2023
    version of the database. Documentation examples show how many baseball
    questions can be investigated.
	"""
	
	homepage = "https://CRAN.R-project.org/package=Lahman"
	cran = "Lahman" 

	version("11.0-0", md5="7e2da648fa7c2e3f7af3dc82b5487559")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
