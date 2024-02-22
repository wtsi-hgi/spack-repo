# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecision(RPackage):
	"""Statistical Decision Analysis

	Contains a function called dmur() which accepts four parameters like possible values, probabilities of the values, selling cost and preparation cost. The dmur() function generates various numeric decision parameters like MEMV (Maximum (optimum) expected monitory value), best choice, EPPI (Expected profit with perfect information), EVPI (Expected value of the perfect information), EOL (Expected opportunity loss), which facilitate effective decision-making.
	"""
	
	cran = "decision" 

	version("0.1.0", md5="2a3aee287493c5b724ed40970a24624b")

