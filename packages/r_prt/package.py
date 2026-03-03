# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrt(RPackage):
	"""Tabular Data Backed by Partitioned 'fst' Files

	Intended for larger-than-memory tabular data, 'prt' objects provide an interface to read row and/or column subsets into memory as data.table objects. Data queries, constructed as 'R' expressions, are evaluated using the non-standard evaluation framework provided by 'rlang' and file-backing is powered by the fast and efficient 'fst' package.
	"""
	
	homepage = "https://nbenn.github.io/prt/"
	cran = "prt" 

	version("0.2.0", md5="6cdd7c6fc6aca40fbfc1973aa7490ef5")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-pillar@1.7:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
