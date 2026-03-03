# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHcandersenr(RPackage):
	"""H.C. Andersens Fairy Tales

	Texts for H.C. Andersens fairy tales, ready for
    text analysis. Fairy tales in German, Danish, English, Spanish and
    French.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/hcandersenr"
	cran = "hcandersenr" 

	version("0.2.0", md5="0c2202adf98ba59ddaf8f98cb73c4dc0")

	depends_on("r@3:", type=("build", "run"))
