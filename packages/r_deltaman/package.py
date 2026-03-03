# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeltaman(RPackage):
	"""Delta Measurement of Agreement for Nominal Data

	Analysis of agreement for nominal data between two raters using the Delta model. This model is proposed as an alternative to the widespread measure Cohen kappa coefficient, which performs poorly when the marginal distributions are very asymmetric (Martin-Andres and Femia-Marzo (2004), <doi:10.1348/000711004849268>; Martin-Andres and Femia-Marzo (2008) <doi:10.1080/03610920701669884>). The package also contains a function to perform a massive analysis of multiple raters against a gold standard. A shiny app is also provided to obtain the measures of nominal agreement between two raters.
	"""
	
	cran = "DeltaMAN" 

	version("0.5.0", md5="e99f8565f54a13e6f430d3cf0c96e6cb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinymatrix", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
