# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordler(RPackage):
	"""The 'WORDLE' Game

	The 'Wordle' game. Players have six attempts to guess a 
    five-letter word. After each guess, the player is informed which 
    letters in their guess are either: anywhere in the word; in the right 
    position in the word. This can be used to inform the next guess. Can be 
    played interactively in the console, or programmatically. Based on Josh 
    Wardle's game <https://www.powerlanguage.co.uk/wordle/>.
	"""
	
	homepage = "https://github.com/DavidASmith/wordler"
	cran = "wordler" 

	version("0.3.1", md5="dd2bdeea3e22848071802a26d5140c8f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
