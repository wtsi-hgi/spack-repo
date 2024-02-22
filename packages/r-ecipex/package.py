# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcipex(RPackage):
	"""Efficient Calculation of Fine Structure Isotope Patterns via
Fourier Transforms of Simplex-Based Elemental Models

	Provides a function that quickly computes the fine structure
    isotope patterns of a set of chemical formulas to a given degree of
    accuracy (up to the limit set by errors in floating point arithmetic). A
    data-set comprising the masses and isotopic abundances of individual
    elements is also provided and calculation of isotopic gross structures
    is also supported.
	"""
	
	cran = "ecipex" 

	version("1.1", md5="b8c455e4fab0df185003f508ca43a50f")

	depends_on("r-chnosz", type=("build", "run"))
