# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawscore(RPackage):
	"""Pain Assessment at Withdrawal Speeds (PAWS)

	Automated pain scoring from paw withdrawal tracking data. Based on
             Jones et al. (2020) "A machine-vision approach for automated pain
             measurement at millisecond timescales" <doi:10.7554/eLife.57258>.
	"""
	
	cran = "pawscore" 

	version("1.0.3", md5="cb06423a3e95e45a6a9320d69f0f286e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-brglm2@0.6:", type=("build", "run"))
	depends_on("r-signal@0.7:", type=("build", "run"))
