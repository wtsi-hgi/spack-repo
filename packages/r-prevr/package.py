# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrevr(RPackage):
	"""Estimating Regional Trends of a Prevalence from a DHS and
Similar Surveys

	Spatial estimation of a prevalence surface
    or a relative risks surface, using data from a Demographic and Health
    Survey (DHS) or an analog survey, see Larmarange et al. (2011)
    <doi:10.4000/cybergeo.24606>.
	"""
	
	homepage = "https://github.com/larmarange/prevR/"
	cran = "prevR" 

	version("5.0.0", md5="516c49a2dad11a08030115d6b54f2380")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-directlabels", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
