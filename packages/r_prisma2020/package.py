# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrisma2020(RPackage):
	"""Make Interactive 'PRISMA' Flow Diagrams

	Systematic reviews should be described in a high degree of 
    methodological detail. The 'PRISMA' Statement calls for a high level of 
    reporting detail in systematic reviews and meta-analyses. An integral part 
    of the methodological description of a review is a flow diagram. 
    This package produces an interactive flow diagram that conforms to the 
    'PRISMA2020' preprint. When made interactive, the reader/user can click 
    on each box and be directed to another website or file online (e.g. a 
    detailed description of the screening methods, or a list of excluded full 
    texts), with a mouse-over tool tip that describes the information linked 
    to in more detail. Interactive versions can be saved as HTML files, 
    whilst static versions for inclusion in manuscripts can be saved as 
    HTML, PDF, PNG, SVG, PS or WEBP files.
	"""
	
	cran = "PRISMA2020" 

	version("1.1.1", md5="a4979c301f28d91912851083f2d1b9df", url="https://cran.r-project.org/src/contrib/PRISMA2020_1.1.1.tar.gz")

	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-diagrammersvg", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-webp", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
