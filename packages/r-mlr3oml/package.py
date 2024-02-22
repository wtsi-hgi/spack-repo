# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3oml(RPackage):
	"""Connector Between 'mlr3' and 'OpenML'

	Provides an interface to 'OpenML.org' to list and download
    machine learning data, tasks and experiments. The 'OpenML' objects can
    be automatically converted to 'mlr3' objects.  For a more
    sophisticated interface with more upload options, see
    the 'OpenML' package.
	"""
	
	homepage = "https://mlr3oml.mlr-org.com"
	cran = "mlr3oml" 

	version("0.9.0", md5="1a0bddebf2bef278d401bf1c2a7b4d79")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-backports@1.1.6:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-mlr3@0.16:", type=("build", "run"))
	depends_on("r-mlr3misc@0.7:", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
