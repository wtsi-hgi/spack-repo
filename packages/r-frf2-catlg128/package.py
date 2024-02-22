# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrf2Catlg128(RPackage):
	"""Catalogues of Resolution IV 128 Run 2-Level Fractional
Factorials Up to 33 Factors that Do Have 5-Letter Words

	Catalogues of resolution IV regular
        fractional factorial designs in 128 runs are provided 
        for up to 33 2-level factors. The catalogues are complete, 
        excluding resolution IV designs without 5-letter words, 
        because these do not add value for a search for unblocked 
        clear designs. The previous package version
        1.0 with complete catalogues up to 24 runs (24 runs and a
        namespace added later) can be downloaded from the authors
        website.
	"""
	
	homepage = "https://prof.bht-berlin.de/groemping/DoE/"
	cran = "FrF2.catlg128" 

	version("1.2-3", md5="93781fa4cf3cdc77e249d63dcece4bd0", url="https://cran.r-project.org/src/contrib/FrF2.catlg128_1.2-3.tar.gz")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-frf2@1.4:", type=("build", "run"))
