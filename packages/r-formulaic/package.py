# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormulaic(RPackage):
	"""Dynamic Generation and Quality Checks of Formula Objects

	Many statistical models and analyses in R are implemented through formula objects. The formulaic package creates a unified approach for programmatically and dynamically generating formula objects. Users may specify the outcome and inputs of a model directly, search for variables to include based upon naming patterns, incorporate interactions, and identify variables to exclude. A wide range of quality checks are implemented to identify issues such as misspecified variables, duplication, a lack of contrast in the inputs, and a large number of levels in categorical data.  Variables that do not meet these quality checks can be automatically excluded from the model.  These issues are documented and reported in a manner that provides greater accountability and useful information to guide an investigation of the data.
	"""
	
	homepage = "https://dachosen1.github.io/formulaic/index.html"
	cran = "formulaic" 

	version("0.0.8", md5="a64427f7d75e9cda45a0689fc4e15ae6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
