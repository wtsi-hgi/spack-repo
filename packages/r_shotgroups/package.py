# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShotgroups(RPackage):
	"""Analyze Shot Group Data

	Analyzes shooting data with respect to group shape,
        precision, and accuracy. This includes graphical methods,
        descriptive statistics, and inference tests using standard,
        but also non-parametric and robust statistical methods.
        Implements distributions for radial error in bivariate normal
        variables. Works with files exported by 'OnTarget PC/TDS',
        'Silver Mountain' e-target, 'ShotMarker' e-target, or 'Taran',
        as well as with custom data files in text format.
        Supports inference from range statistics such as extreme
        spread. Includes a set of web-based graphical user interfaces.
	"""
	
	cran = "shotGroups" 

	version("0.8.2", md5="87b94bdd0b5be6eec069120802e62215")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-compquadform@1.4.2:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
