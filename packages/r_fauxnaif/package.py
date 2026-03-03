# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFauxnaif(RPackage):
	"""Convert Values to NA

	Provides a replacement for dplyr::na_if().  Allows you to
    specify multiple values to be replaced with NA using a single
    function.
	"""
	
	homepage = "https://fauxnaif.rossellhayes.com/"
	cran = "fauxnaif" 

	version("0.7.1", md5="e665a106d410a047b43872a0bdb504e1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
