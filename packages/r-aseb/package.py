# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAseb(RPackage):
	"""Predict Acetylated Lysine Sites

	ASEB is an R package to predict lysine sites that can be acetylated by a specific KAT-family.
	"""
	
	bioc = "ASEB"

	version("1.52.0", commit="fa6f28a9a2fc571547eccb2c329931cd49e23123")
	version("1.46.3", commit="99edb08fe5b0f390f7a0d77c5fcea0e5dcc31275")

	depends_on("r@2.8:", type=("build", "run"))
