# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFish(RPackage):
	"""Fisher-Shannon Method

	Proposes non-parametric estimates of the Fisher information measure and the 
              Shannon entropy power. More theoretical and implementation details can be found
              in Guignard et al. <doi:10.3389/feart.2020.00255>. A 'python' version of this
              work is available on 'github' and 'PyPi' ('FiShPy').
	"""
	
	cran = "FiSh" 

	version("1.1", md5="07d4bf5f5bffa1a1aba0100c47fa8a60")

	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
