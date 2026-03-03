# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSftools(RPackage):
	"""Space Filling Based Tools for Data Mining

	Contains space filling based tools for
    machine learning and data mining. Some functions offer
    several computational techniques and deal with the out of
    memory for large big data by using the ff package.
	"""
	
	homepage = "https://sites.google.com/site/mohamedlaibwebpage/"
	cran = "SFtools" 

	version("0.1.0", md5="5f11b6efc50f414f6da030f5d176df49")

	depends_on("r-wordspace", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
