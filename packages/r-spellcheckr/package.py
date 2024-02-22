# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpellcheckr(RPackage):
	"""Correct the Spelling of a Given Word in the English Language

	Corrects the spelling of a given word in English 
    using a modification of Peter Norvig's spell correct 
    algorithm (see <http://norvig.com/spell-correct.html>) 
    which handles up to three edits. The algorithm tries to 
    find the spelling with maximum probability of intended
    correction out of all possible candidate corrections from
    the original word.
	"""
	
	cran = "spellcheckr" 

	version("0.1.2", md5="9c0f08c5a8bc3ecedbe5dff8006efd68")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
