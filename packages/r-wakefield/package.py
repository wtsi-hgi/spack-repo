# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWakefield(RPackage):
	"""Generate Random Data Sets

	Generates random data sets including: data.frames, lists,
        and vectors.
	"""
	
	homepage = "https://github.com/trinker/wakefield"
	cran = "wakefield" 

	version("0.3.6", md5="09c345564f8174ba30f49c593917bc5f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
