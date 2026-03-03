# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAudiometry(RPackage):
	"""Standard Conform Pure Tone Audiometry (PTA) Plots

	Facilitates plotting audiometric data (mostly) by preparing the coordinate system according to standards, given e. g. in American Speech-Language-Hearing Association (2005), <doi:10.1044/policy.GL2005-00014>.
	"""
	
	cran = "audiometry" 

	version("0.3.0", md5="f4b981baab7e5a4fbac2a4111b7f112a")

	depends_on("r-ggplot2", type=("build", "run"))
