# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsmtools(RPackage):
	"""Building Augmented Data to Run Multi-State Models with 'msm'
Package

	A fast and general method for restructuring classical longitudinal data into
    augmented ones. The reason for this is to facilitate the modeling of longitudinal data under
    a multi-state framework using the 'msm' package.
	"""
	
	homepage = "https://github.com/contefranz/msmtools"
	cran = "msmtools" 

	version("2.0.1", md5="2c20cc83bc3ea299d63b4e13af8618eb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-msm@1.6:", type=("build", "run"))
	depends_on("r-survival@2.38:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-patchwork@1.1.1:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
