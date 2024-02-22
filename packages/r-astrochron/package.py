# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAstrochron(RPackage):
	"""A Computational Tool for Astrochronology

	Routines for astrochronologic testing, astronomical time scale construction, and time series analysis <doi:10.1016/j.earscirev.2018.11.015>. Also included are a range of statistical analysis and modeling routines that are relevant to time scale development and paleoclimate analysis.
	"""
	
	cran = "astrochron" 

	version("1.2", md5="844971594aa27fd83b24bc7707eb3a1b")

	depends_on("r-multitaper", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-idpmisc", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-palinsol", type=("build", "run"))
