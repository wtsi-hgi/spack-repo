# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAllcontributors(RPackage):
	"""Acknowledge all Contributors to a Project

	Acknowledge all contributors to a project via a single
    function call. The function appends to a 'README' or other specified
    file(s) a table with names of all individuals who contributed via code
    or repository issues.  The package also includes several additional
    functions to extract and quantify contributions to any repository.
	"""
	
	homepage = "https://github.com/ropenscilabs/allcontributors"
	cran = "allcontributors" 

	version("0.1.1", md5="af40049fec902483a5edfd0d2d311a95")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-gitcreds", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
