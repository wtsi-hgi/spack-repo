# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsafe(RPackage):
	"""Surrogate-Assisted Feature Extraction

	Provides a model agnostic tool for white-box model trained on features extracted from a black-box model. For more information see: Gosiewska et al. (2020) <doi:10.1016/j.dss.2021.113556>.
	"""
	
	homepage = "https://github.com/ModelOriented/rSAFE"
	cran = "rSAFE" 

	version("0.1.4", md5="f9d76b82fe16b4c277852851cd2f0a66")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ingredients", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
