# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntsdm(RPackage):
	"""Reproducible Integrated Species Distribution Models Across
Norway using 'INLA'

	Integration of disparate datasets is needed in order to make efficient use of all available data and thereby address the issues currently threatening biodiversity.
   Data integration is a powerful modeling framework which allows us to combine these datasets together into a single model, yet retain the strengths of each individual dataset.
   We therefore introduce the package, 'intSDM': an R package designed to help ecologists develop a reproducible workflow of integrated species distribution models, using data both provided from the user as well as data obtained freely online.
   An introduction to data integration methods is discussed in Issac, Jarzyna, Keil, Dambly, Boersch-Supan, Browning, Freeman, Golding, Guillera-Arroita, Henrys, Jarvis, Lahoz-Monfort, Pagel, Pescott, Schmucki, Simmonds and O’Hara (2020) <doi:10.1016/j.tree.2019.08.006>.
	"""
	
	cran = "intSDM" 

	version("2.0.2", md5="9edc7078f22340005235dadd328225cd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-pointedsdms", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-geodata", type=("build", "run"))
	depends_on("r-inlabru@2.3.1:", type=("build", "run"))
	depends_on("r-giscor", type=("build", "run"))
	depends_on("r-blockcv", type=("build", "run"))
	depends_on("r-rgbif", type=("build", "run"))
	depends_on("r-tidyterra", type=("build", "run"))
