# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRicu(RPackage):
	"""Intensive Care Unit Data with R

	Focused on (but not exclusive to) data sets hosted on PhysioNet
    (<https://physionet.org>), 'ricu' provides utilities for download, setup
    and access of intensive care unit (ICU) data sets. In addition to
    functions for running arbitrary queries against available data sets, a
    system for defining clinical concepts and encoding their representations
    in tabular ICU data is presented.
	"""
	
	homepage = "https://github.com/eth-mds/ricu"
	cran = "ricu" 

	version("0.5.6", md5="542992903eb5c23228c6ddd420604bda")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-prt@0.1.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-cli@2.1:", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
