# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegday(RPackage):
	"""Compute Degree Days

	Compute degree days from daily min and max temperatures for
    modeling plant and insect development.
	"""
	
	homepage = "https://github.com/ucanr-igis/degday/"
	cran = "degday" 

	version("0.4.0", md5="9a8af8c44806acc9c3501b3a4ed2ef1e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
