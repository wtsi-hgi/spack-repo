# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdpmisc(RPackage):
	"""'Utilities of Institute of Data Analyses and Process Design
(www.zhaw.ch/idp)'

	Different high-level graphics functions for displaying large datasets, displaying circular data in a very flexible way, finding local maxima, brewing color ramps, drawing nice arrows, zooming 2D-plots, creating figures with differently colored margin and plot region.  In addition, the package contains auxiliary functions for data manipulation like omitting observations with irregular values or selecting data by logical vectors, which include NAs. Other functions are especially useful in spectroscopy and analyses of environmental data: robust baseline fitting, finding peaks in spectra, converting humidity measures.
	"""
	
	cran = "IDPmisc" 

	version("1.1.21", md5="2e7d6fc2c0921903a1a584bacf9af609")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
