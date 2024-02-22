# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3misc(RPackage):
	"""Helper Functions for 'mlr3'

	Frequently used helper functions and assertions used in
    'mlr3' and its companion packages. Comes with helper functions for
    functional programming, for printing, to work with 'data.table', as
    well as some generally useful 'R6' classes. This package also
    supersedes the package 'BBmisc'.
	"""
	
	homepage = "https://mlr3misc.mlr-org.com"
	cran = "mlr3misc" 

	version("0.14.0", md5="6a2ea3fc5360bbbf52bf699266b9c2c3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-backports@0.1.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
