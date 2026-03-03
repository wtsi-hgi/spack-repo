# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdinalcont(RPackage):
	"""Ordinal Regression Analysis for Continuous Scales

	A regression framework for response variables which are continuous
    self-rating scales such as the Visual Analog Scale (VAS) used in pain
    assessment, or the Linear Analog Self-Assessment (LASA) scales in quality
    of life studies. These scales measure subjects' perception of an intangible
    quantity, and cannot be handled as ratio variables because of their inherent
    non-linearity. We treat them as ordinal variables, measured on a continuous
    scale. A function (the g function) connects the scale with an underlying
    continuous latent variable. The link function is the inverse of the CDF of the
    assumed underlying distribution of the latent variable. A variety of
    link functions are currently implemented. Such models are described in Manuguerra et al (2020) <doi:10.18637/jss.v096.i08>.
	"""
	
	cran = "ordinalCont" 

	version("2.0.2", md5="328b2008f71942431c30aa0d3994302d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
