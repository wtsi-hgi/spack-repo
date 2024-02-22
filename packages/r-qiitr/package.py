# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQiitr(RPackage):
	"""R Interface to Qiita API

	Qiita is a technical knowledge sharing and collaboration platform for programmers.
  See <https://qiita.com/api/v2/docs> for more information.
	"""
	
	homepage = "https://github.com/yutannihilation/qiitr"
	cran = "qiitr" 

	version("0.1.1", md5="b913be0cb3365f023ea80803a07fbf5e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
