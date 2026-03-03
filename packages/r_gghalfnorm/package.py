# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGghalfnorm(RPackage):
	"""Create a Half Normal Plot Using 'ggplot2'

	Reproduce the halfnorm() function found in the 'faraway' package 
    using the 'ggplot2' API.
	"""
	
	homepage = "https://github.com/nathaneastwood/gghalfnorm"
	cran = "gghalfnorm" 

	version("1.1.2", md5="4e04d4e5428325a6111effa18c7865cb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-ggrepel@0.6.5:", type=("build", "run"))
