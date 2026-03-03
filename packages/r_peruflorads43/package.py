# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeruflorads43(RPackage):
	"""Reviewed Official Classification of Endangered Wild Flora
Species in Peru

	Provide users with a convenient way to access and analyze information on endangered plant species in Peru based on `Decreto Supremo N 043-2006-AG - Aprueban categorizacion de especies amenazadas de flora silvestre`<https://sinia.minam.gob.pe/normas/aprueban-categorizacion-especies-amenazadas-flora-silvestre>.
	"""
	
	homepage = "https://github.com/PaulESantos/peruflorads43"
	cran = "peruflorads43" 

	version("0.1.1", md5="96511186e8378471d5727ccdab7474ec", url="https://cran.r-project.org/src/contrib/peruflorads43_0.1.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
