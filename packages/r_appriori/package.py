# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAppriori(RPackage):
	"""Code and Obtain Customized Planned Comparisons with 'appRiori'

	With 'appRiori', users upload the research variables and the app guides them to the best set of comparisons fitting the hypotheses, for both main and interaction effects. Through a graphical explanation and empirical examples on reproducible data, it is shown that it is possible to understand both the logic behind the planned comparisons and the way to interpret them when a model is tested.
	"""
	
	homepage = "https://github.com/Ugranziol/appRiori"
	cran = "appRiori" 

	version("0.0.5", md5="3f50b345803c91ebbfb425744878d774")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-hypr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-sortable", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
