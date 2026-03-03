# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUssherr(RPackage):
	"""Ussher Data Set Drawn from 1658 Chronology

	The "ussher" data set is drawn from original chronological textual historic events. Commonly known as James Ussher's Annals of the World, the source text was originally written in Latin in 1650, and published in English translation in 1658.The data are classified by index, year, epoch (or one of the 7 ancient "Ages of the World"), Biblical source book if referenced (rarely), as well as alternate dating mechanisms, such as "Anno Mundi" (age of the world) or "Julian Period" (dates based upon the Julian calendar). Additional file "usshfull" includes variables that may be of further interest to historians, such as Southern Kingdom and Northern Kingdom discrepant dates, and the original amalgamated dating mechanic used by Ussher in the original text. The raw data can also be called using "usshraw", as described in: Ussher, J. (1658) <https://archive.org/stream/AnnalsOfTheWorld/Annals_djvu.txt>.
	"""
	
	cran = "ussherR" 

	version("1.10", md5="6d0c249c6ca72075b68d791704ac33c3")

	depends_on("r@2.10:", type=("build", "run"))
