# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFis(RPackage):
	"""Human Functional Interactions (FIs) for splineTimeR package

	Data set containing two complete lists of identified functional interaction partners in Human. Data are derived from Reactome and BioGRID databases.
	"""
	
	bioc = "FIs"

	version("1.36.0", commit="7fcfae89bb061af6633c0c3f5cabe2d9df5340ae")
	version("1.30.0", commit="6ebc57f7cc1ffbc3f986eb96d1baf4a1b44bd3a7")

	depends_on("r@3.3:", type=("build", "run"))

