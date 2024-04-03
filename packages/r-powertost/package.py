# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowertost(RPackage):
	"""Power and Sample Size for (Bio)Equivalence Studies

	Contains functions to calculate power and sample size for
    various study designs used in bioequivalence studies. Use known.designs() to
    see the designs supported. Power and sample size can be obtained based on
    different methods, amongst them prominently the TOST procedure (two one-sided
    t-tests). See README and NEWS for further information.
	"""
	
	homepage = "https://github.com/Detlew/PowerTOST"
	cran = "PowerTOST" 

	version("1.5-6", md5="836d429f511147af06d3ff12fd040981")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cubature@1.3.6:", type=("build", "run"))
