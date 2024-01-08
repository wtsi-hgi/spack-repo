# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RPrediction(RPackage):
	"""Tidy, Type-Safe 'prediction()' Methods

	A one-function package containing 'prediction()', a type-safe alternative to 'predict()' that always returns a data frame. The 'summary()' method provides a data frame with average predictions, possibly over counterfactual versions of the data (a la the 'margins' command in 'Stata'). Marginal effect estimation is provided by the related package, 'margins' <https://cran.r-project.org/package=margins>. The package currently supports common model types (e.g., "lm", "glm") from the 'stats' package, as well as numerous other model classes from other add-on packages. See the README or main package documentation page for a complete listing.
	"""
	
	homepage = "https://github.com/leeper/prediction"
	cran = "prediction" 

	version("0.3.14", md5="f27a713e1265ac86ab47b06a32154e44")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
