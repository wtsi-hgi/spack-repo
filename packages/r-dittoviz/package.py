# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDittoviz(RPackage):
	"""User Friendly Data Visualization

	A comprehensive visualization toolkit built with coders of all
    skill levels and color-vision impaired audiences in mind. It allows creation
    of finely-tuned, publication-quality figures from single function calls.
    Visualizations include scatter plots, compositional bar plots, violin, box,
    and ridge plots, and more. Customization ranges from size and title
    adjustments to discrete-group circling and labeling, hidden data overlay
    upon cursor hovering via ggplotly() conversion, and many more, all with
    simple, discrete inputs. Color blindness friendliness is powered by legend
    adjustments (enlarged keys), and by allowing the use of shapes or
    letter-overlay in addition to the carefully selected dittoColors().
	"""
	
	homepage = "https://github.com/dtm2451/dittoViz"
	cran = "dittoViz" 

	version("1.0.1", md5="16df4d3c211fadec13bdeb287e2a04e2")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
