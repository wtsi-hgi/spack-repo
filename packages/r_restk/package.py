# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestk(RPackage):
	"""An Implementation of the RESTK Algorithm

	Implementation of the RESTK algorithm based on Markov's Inequality from  Vilardell, Sergi, Serra, Isabel, Mezzetti, Enrico, Abella, Jaume, Cazorla, Francisco  J. and Del Castillo, J. (2022). "Using Markov's Inequality with Power-Of-k Function for Probabilistic WCET Estimation". In 34th Euromicro Conference on Real-Time Systems (ECRTS 2022). Leibniz International Proceedings in Informatics (LIPIcs) 231 20:1-20:24. <doi:10.4230/LIPIcs.ECRTS.2022.20>. This work has been supported by the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No. 772773).
	"""
	
	cran = "RESTK" 

	version("1.0.0", md5="bbf65350477ada093d37d88ff377357e")

	depends_on("r-purrr", type=("build", "run"))
