# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZipsae(RPackage):
	"""Small Area Estimation with Zero-Inflated Model

	This function produces empirical best linier unbiased predictions (EBLUPs) for Zero-Inflated data and its Relative Standard Error. Small Area Estimation with Zero-Inflated Model (SAE-ZIP) is a model developed for Zero-Inflated data that can lead us to overdispersion situation. To handle this kind of situation, this model is created. The model in this package is based on Small Area Estimation with Zero-Inflated Poisson model proposed by Dian Christien Arisona (2018)<https://repository.ipb.ac.id/handle/123456789/92308>. For the data sample itself, we use combination method between Roberto Benavent and Domingo Morales (2015)<doi:10.1016/j.csda.2015.07.013> and Sabine Krieg, Harm Jan Boonstra and Marc Smeets (2016)<doi:10.1515/jos-2016-0051>.
	"""
	
	homepage = "https://github.com/dheel/zipsae"
	cran = "zipsae" 

	version("1.0.2", md5="9117389e38f78b005ff4141edf20220e")

	depends_on("r@2.10:", type=("build", "run"))
