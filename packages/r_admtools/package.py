# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmtools(RPackage):
	"""Estimate and Manipulate Age-Depth Models

	Estimate age-depth models from stratigraphic and sedimentological data,
    and transform data
    between the time and stratigraphic domain.
	"""
	
	homepage = "https://github.com/MindTheGap-ERC/admtools"
	cran = "admtools" 

	version("0.2.0", md5="45c548bd7766b399652357cf45a0896f")
	version("0.1.0", md5="c2bc10bffa289b438300140ad7b12e09")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
