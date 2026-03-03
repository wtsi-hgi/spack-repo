# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChinesenames(RPackage):
	"""Chinese Name Database 1930-2008

	
    A database of Chinese surnames and Chinese given names (1930-2008).
    This database contains nationwide frequency statistics of
    1,806 Chinese surnames and 2,614 Chinese characters used in given names,
    covering about 1.2 billion Han Chinese population
    (96.8% of the Han Chinese household-registered population
    born from 1930 to 2008 and still alive in 2008).
    This package also contains a function for computing multiple features of
    Chinese surnames and Chinese given names for scientific research (e.g.,
    name uniqueness, name gender, name valence, and name warmth/competence).
	"""
	
	homepage = "https://psychbruce.github.io/ChineseNames/"
	cran = "ChineseNames" 

	version("2023.8", md5="28f71933901bef716785878ba98ea1ed")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-brucer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
