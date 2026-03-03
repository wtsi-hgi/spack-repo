# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiversificationr(RPackage):
	"""Econometric Tools to Measure Portfolio Diversification

	Diversification is one of the most important concepts in portfolio management. This framework offers scholars, practitioners and policymakers a useful toolbox to measure diversification. Specifically, this framework provides recent diversification measures from the recent literature. These diversification measures are based on the works of Rudin and Morgan (2006) <doi:10.3905/jpm.2006.611807>, Choueifaty and Coignard (2008) <doi:10.3905/JPM.2008.35.1.40>, Vermorken et al. (2012) <doi:10.3905/jpm.2012.39.1.067>, Flores et al. (2017) <doi:10.3905/jpm.2017.43.4.112>, Calvet et al. (2007) <doi:10.1086/524204>, and Candelon, Fuerst and Hasse (2020).
	"""
	
	cran = "DiversificationR" 

	version("0.1.0", md5="a6459a696446bfba21992913c3d6f642")

	depends_on("r@2.10:", type=("build", "run"))
