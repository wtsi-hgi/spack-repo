# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffectstars2(RPackage):
	"""Effect Stars

	Provides functions for the method of effect stars as proposed by Tutz and Schauberger (2013) <doi:10.1080/10618600.2012.701379>. Effect stars can be used to visualize estimates of parameters corresponding to different groups, for example in multinomial logit models. Beside the main function 'effectstars' there exist methods for special objects, for example for 'vglm' objects from the 'VGAM' package.
	"""
	
	cran = "EffectStars2" 

	version("0.1-3", md5="dc90be3ecb2662db701ac821265dc38a", url="https://cran.r-project.org/src/contrib/EffectStars2_0.1-3.tar.gz")

	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
