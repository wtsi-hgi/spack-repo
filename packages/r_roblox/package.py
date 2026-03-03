# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoblox(RPackage):
	"""Optimally Robust Influence Curves and Estimators for Location
and Scale

	Functions for the determination of optimally robust influence curves and
             estimators in case of normal location and/or scale 
             (see Chapter 8 in Kohl (2005) <https://epub.uni-bayreuth.de/839/2/DissMKohl.pdf>).
	"""
	
	homepage = "http://robast.r-forge.r-project.org/"
	cran = "RobLox" 

	version("1.2.1", md5="b90d0b6bd946b247727dd98bda76d802")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distrmod@2.8:", type=("build", "run"))
	depends_on("r-robastbase@1.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-randvar@1.2:", type=("build", "run"))
	depends_on("r-distr@2.8:", type=("build", "run"))
