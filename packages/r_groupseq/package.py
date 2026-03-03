# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroupseq(RPackage):
	"""Group Sequential Design Probabilities - With Graphical User
Interface

	Computes probabilities related to group sequential designs for
    normally distributed test statistics. Enables to derive critical
    boundaries, power, drift, and confidence intervals of such designs.
    Supports the alpha spending approach by Lan-DeMets (1994)
    <doi:10.1002/sim.4780131308>.
	"""
	
	homepage = "https://rpahl.github.io/GroupSeq/"
	cran = "GroupSeq" 

	version("1.4.3", md5="2e8a4891bd7937ca18f2ea89b5e5f673")

	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
