# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastlaplace(RPackage):
	"""A Fast Laplace Method for Spatial Generalized Linear Mixed Model

	Fitting a fast Laplace approximation for Spatial Generalized Linear Mixed Model as
  described in Park and Lee (2021) <https://github.com/sangwan93/fastLaplace/blob/main/FastLaplaceMain.pdf>.
	"""
	
	homepage = "<https://www.naver.com/>"
	cran = "fastLaplace" 

	version("0.0.2", md5="83f50bd2fd7a260f8d6d1979bee134df")

	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
