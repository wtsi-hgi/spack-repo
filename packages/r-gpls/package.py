# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpls(RPackage):
	"""Classification using generalized partial least squares

	Classification using generalized partial least squares for two-group and multi-group (more than 2 group) classification.
	"""
	
	bioc = "gpls"

	version("1.80.0", commit="2abfe1c9d00191e3133589982251be2df35bfde8")
	version("1.74.0", commit="85e2138d0e5debecc473cd2879a2fe01bf08126c")

