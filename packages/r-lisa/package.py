# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLisa(RPackage):
	"""Color Palettes from Color Lisa

	Contains 128 palettes from Color Lisa. All palettes are based on 
    masterpieces from the worlds greatest artists. For more information, see 
    <http://colorlisa.com/>.
	"""
	
	homepage = "https://github.com/tyluRp/lisa"
	cran = "lisa" 

	version("0.1.2", md5="dada407c93f783ad876dae1fdd7c5b02")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
