# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyrules(RPackage):
	"""Obtain Rules from Rule Based Models as Tidy Dataframe

	Utility to convert text based summary of rule based models to a tidy dataframe (where each row represents a rule) with related metrics such as support, confidence and lift. Rule based models from these packages are supported: 'C5.0', 'rpart' and 'Cubist'.
	"""
	
	homepage = "https://github.com/talegari/tidyrules"
	cran = "tidyrules" 

	version("0.1.5", md5="27919ac86cf9087fb86bbe0bf0888f77")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tibble@2.0.1:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-partykit@1.2.2:", type=("build", "run"))
