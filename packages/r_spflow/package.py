# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpflow(RPackage):
	"""Spatial Econometric Interaction Models

	
    Efficient estimation of spatial econometric models of origin-destination flows, which may exhibit spatial autocorrelation in the dependent variable, the explanatory variables or both.
    The model is the one proposed by LeSage and Pace (2008) <doi:10.1111/j.1467-9787.2008.00573.x>, who develop a matrix formulation that exploits the relational structure of flow data.
    The estimation procedures follow most closely those outlined by Dargel (2021) (preprint available at <https://www.tse-fr.eu/fr/publications/revisiting-estimation-methods-spatial-econometric-interaction-models>).
	"""
	
	homepage = "https://github.com/LukeCe/spflow"
	cran = "spflow" 

	version("0.1.0", md5="98ef62e6a5adc257baf30ae165687cac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
