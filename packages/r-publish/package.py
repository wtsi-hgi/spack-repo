# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPublish(RPackage):
	"""Format Output of Various Routines in a Suitable Way for Reports
and Publication

	A bunch of convenience functions that transform the results of some basic statistical analyses
       into table format nearly ready for publication. This includes descriptive tables, tables of
       logistic regression and Cox regression results as well as forest plots. 
	"""
	
	cran = "Publish" 

	version("2023.01.17", md5="9d72efa9e09fa009b0fd25fb388e7f79")

	depends_on("r-prodlim@1.5.4:", type=("build", "run"))
	depends_on("r-survival@2.38:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-lava@1.5.1:", type=("build", "run"))
	depends_on("r-multcomp@1.4:", type=("build", "run"))
