# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKdry(RPackage):
	"""K's "Don't Repeat Yourself"-Collection

	A collection of personal helper functions to avoid redundancy
    in the spirit of the "Don't repeat yourself" principle of software
    development (<https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>).
	"""
	
	homepage = "https://github.com/kapsner/kdry"
	cran = "kdry" 

	version("0.0.2", md5="2573312a73816e477a28a8ebcf0097dc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
