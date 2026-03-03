# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpartaas(RPackage):
	"""Statistical Pattern Recognition and daTing using Archaeological
Artefacts assemblageS

	Statistical pattern recognition and dating using archaeological artefacts assemblages.
    Package of statistical tools for archaeology.
    hclustcompro(perioclust): Bellanger Lise, Coulon Arthur, Husi Philippe (2021, ISBN:978-3-030-60103-4).
    mapclust: Bellanger Lise, Coulon Arthur, Husi Philippe (2021) <doi:10.1016/j.jas.2021.105431>.
    seriograph: Desachy Bruno (2004) <doi:10.3406/pica.2004.2396>.
    cerardat: Bellanger Lise, Husi Philippe (2012) <doi:10.1016/j.jas.2011.06.031>.
	"""
	
	homepage = "https://spartaas.gitpages.huma-num.fr/r-package/"
	cran = "SPARTAAS" 

	version("1.2.1", md5="dd0203dee18196b6196880f2d0890ba2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinyjqui", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-explor", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-scatterd3", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-mapview", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-nor1mix", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
