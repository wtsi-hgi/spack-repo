# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaneaustenr(RPackage):
	"""Jane Austen's Complete Novels

	Full texts for Jane Austen's 6 completed novels, ready for
    text analysis. These novels are "Sense and Sensibility", "Pride and
    Prejudice", "Mansfield Park", "Emma", "Northanger Abbey", and
    "Persuasion".
	"""
	
	homepage = "https://github.com/juliasilge/janeaustenr"
	cran = "janeaustenr" 

	version("1.0.0", md5="1e7274a698306174dd9c405b4043ec71")

	depends_on("r@3.5:", type=("build", "run"))
