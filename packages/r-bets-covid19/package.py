# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetsCovid19(RPackage):
	"""The BETS Model for Early Epidemic Data

	Implements likelihood inference for early epidemic analysis. BETS is short for the four key epidemiological events being modeled: Begin of exposure, End of exposure, time of Transmission, and time of Symptom onset. The package contains a dataset of the trajectory of confirmed cases during the coronavirus disease (COVID-19) early outbreak. More detail of the statistical methods can be found in Zhao et al. (2020) <arXiv:2004.07743>.
	"""
	
	homepage = "https://github.com/qingyuanzhao/bets.covid19"
	cran = "bets.covid19" 

	version("1.0.0", md5="6de2cdc1df6445f67b3af272c110c2f2", url="https://cran.r-project.org/src/contrib/bets.covid19_1.0.0.tar.gz")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
