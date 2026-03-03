# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsmodels(RPackage):
	"""Sample Selection Models

	In order to facilitate the adjustment of the sample selection models existing in the literature, we created the 'ssmodels' package. Our package allows the adjustment of the classic Heckman model (Heckman (1976), Heckman (1979) <doi:10.2307/1912352>), and the estimation of the parameters of this model via the maximum likelihood method and two-step method, in addition to the adjustment of the Heckman-t models, introduced in the literature by Marchenko and Genton (2012) <doi:10.1080/01621459.2012.656011> and the Heckman-Skew model introduced in the literature by Ogundimu and Hutton (2016) <doi:10.1111/sjos.12171>. We also implemented functions to adjust the generalized version of the Heckman model, introduced by Bastos, Barreto-Souza, and Genton (2021) <doi:10.5705/ss.202021.0068>, that allows the inclusion of covariables to the dispersion and correlation parameters and a function to adjust the Heckman-BS model introduced by Bastos and Barreto-Souza (2020) <doi:10.1080/02664763.2020.1780570> that uses the Birnbaum-Saunders distribution as a joint distribution of the selection and primary regression variables. 
	"""
	
	cran = "ssmodels" 

	version("1.0.1", md5="446e38199955c708105bf7f86560e77f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sn@2.1:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1.1:", type=("build", "run"))
	depends_on("r-pracma@2.3.8:", type=("build", "run"))
	depends_on("r-misctools@0.6.26:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
