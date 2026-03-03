# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissranger(RPackage):
	"""Fast Imputation of Missing Values

	Alternative implementation of the beautiful 'MissForest'
    algorithm used to impute mixed-type data sets by chaining random
    forests, introduced by Stekhoven, D.J. and Buehlmann, P. (2012)
    <doi:10.1093/bioinformatics/btr597>. Under the hood, it uses the
    lightning fast random jungle package 'ranger'. Between the iterative
    model fitting, we offer the option of using predictive mean matching.
    This firstly avoids imputation with values not already present in the
    original data (like a value 0.3334 in 0-1 coded variable).  Secondly,
    predictive mean matching tries to raise the variance in the resulting
    conditional distributions to a realistic level. This would allow e.g.
    to do multiple imputation when repeating the call to missRanger().  A
    formula interface allows to control which variables should be imputed
    by which.
	"""
	
	homepage = "https://github.com/mayer79/missRanger"
	cran = "missRanger" 

	version("2.4.0", md5="e907ff63e8dc5c9a8bc5da1b5c454789")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
