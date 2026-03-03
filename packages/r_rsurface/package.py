# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsurface(RPackage):
	"""Design of Rotatable Central Composite Experiments and Response
Surface Analysis

	Produces tables with the level of replication (number of replicates) and the
    experimental uncoded values of the quantitative factors to be used for rotatable Central
    Composite Design (CCD) experimentation and a 2-D contour plot of the corresponding
    variance of the predicted response according to
    Mead et al. (2012) <doi:10.1017/CBO9781139020879> design_ccd(), and analyzes
    CCD data with response surface methodology ccd_analysis(). A rotatable CCD
    provides values of the variance of the predicted response that are concentrically
    distributed around the average treatment combination used in the experimentation, which
    with uniform precision (implied by the use of several replicates at the average
    treatment combination) improves greatly the search and finding of an optimum response.
    These properties of a rotatable CCD represent undeniable advantages over the classical
    factorial design, as discussed by Panneton et al. (1999) <doi:10.13031/2013.13267> and
    Mead et al. (2012) <doi:10.1017/CBO9781139020879.018> among others.
	"""
	
	cran = "rsurface" 

	version("1.1.0", md5="ac0c055791f7d46ef3b0df04bb18be21")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rsm", type=("build", "run"))
