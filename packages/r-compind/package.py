# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompind(RPackage):
	"""Composite Indicators Functions

	A collection of functions to calculate Composite Indicators methods, focusing, in particular, on the normalisation and weighting-aggregation steps, as described in OECD Handbook on constructing composite indicators: methodology and user guide <https://www.oecd-ilibrary.org/economics/handbook-on-constructing-composite-indicators-methodology-and-user-guide_9789264043466-en>, 'Vidoli' and 'Fusco' and 'Mazziotta' <doi:10.1007/s11205-014-0710-y>, 'Mazziotta' and 'Pareto' (2016) <doi:10.1007/s11205-015-0998-2>, 'Van Puyenbroeck and 'Rogge' <doi:10.1016/j.ejor.2016.07.038> and other authors.
	"""
	
	cran = "Compind" 

	version("3.0", md5="c2a6efa4f17aa06365089f496566ab1a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-benchmarking", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-nonparaeff", type=("build", "run"))
	depends_on("r-smaa", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-gwmodel", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
