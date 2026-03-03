# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtableicc(RPackage):
	"""Random Generation of Contingency Tables

	Contains functions for random generation of R x C and 2 x 2 x K contingency tables. In addition to the generation of contingency tables over predetermined intraclass-correlated clusters, it is possible to generate contingency tables without intraclass correlations under product multinomial, multinomial, and Poisson sampling plans. It also consists of a function for generation of random data from a given discrete probability distribution function. See Demirhan (2016) <https://journal.r-project.org/archive/2016-1/demirhan.pdf> for more information.
	"""
	
	cran = "rTableICC" 

	version("1.0.9", md5="8dcfbfd09996452cb8cb7ea9150e6d04")

	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-aster", type=("build", "run"))
