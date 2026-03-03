# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3verse(RPackage):
	"""Easily Install and Load the 'mlr3' Package Family

	The 'mlr3' package family is a set of packages for
    machine-learning purposes built in a modular fashion. This wrapper
    package is aimed to simplify the installation and loading of the core
    'mlr3' packages. Get more information about the 'mlr3' project at
    <https://mlr3book.mlr-org.com/>.
	"""
	
	homepage = "https://mlr3verse.mlr-org.com"
	cran = "mlr3verse" 

	version("0.2.8", md5="49119f234d28280dde5ab355d6caff96")

	depends_on("r-mlr3@0.12:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-bbotk", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mlr3cluster", type=("build", "run"))
	depends_on("r-mlr3data", type=("build", "run"))
	depends_on("r-mlr3filters", type=("build", "run"))
	depends_on("r-mlr3fselect@0.8:", type=("build", "run"))
	depends_on("r-mlr3hyperband", type=("build", "run"))
	depends_on("r-mlr3learners", type=("build", "run"))
	depends_on("r-mlr3mbo", type=("build", "run"))
	depends_on("r-mlr3misc@0.11:", type=("build", "run"))
	depends_on("r-mlr3pipelines@0.4:", type=("build", "run"))
	depends_on("r-mlr3tuning@0.17:", type=("build", "run"))
	depends_on("r-mlr3tuningspaces@0.1.1:", type=("build", "run"))
	depends_on("r-mlr3viz", type=("build", "run"))
	depends_on("r-paradox@0.6:", type=("build", "run"))
