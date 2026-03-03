# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfpp(RPackage):
	"""'Matrix-Based Flexible Project Planning'

	Matrix-Based Flexible Project Planning. This package models, plans, and schedules flexible, such as agile, extreme, and hybrid project plans. The package contains project planning, scheduling, and risk assessment functions. Kosztyan (2022) <doi:10.1016/j.softx.2022.100973>.
	"""
	
	homepage = "https://github.com/kzst/mfpp"
	cran = "mfpp" 

	version("0.0.5", md5="d7175aebef51e53ebc4d342d8a9db607")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-nsga2r", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-genalg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
