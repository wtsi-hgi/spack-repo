# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGglgbtq(RPackage):
	"""Show Pride on 'ggplot2' Plots

	Provides multiple palettes based on pride flags with tailored themes.
	"""
	
	homepage = "https://github.com/turtletopia/gglgbtq"
	cran = "gglgbtq" 

	version("0.1.1", md5="0cdd7ec4d254321f8d73a5ac829d5ffd")

	depends_on("r-ggplot2", type=("build", "run"))
