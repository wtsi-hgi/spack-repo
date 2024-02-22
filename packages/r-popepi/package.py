# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopepi(RPackage):
	"""Functions for Epidemiological Analysis using Population Data

	Enables computation of epidemiological statistics, including
    those where counts or mortality rates of the reference population are
    used.  Currently supported: excess hazard models (Dickman, Sloggett,
    Hills, and Hakulinen (2012) <doi:10.1002/sim.1597>), rates, mean
    survival times, relative/net survival (in particular the Ederer II
    (Ederer and Heise (1959)) and Pohar Perme (Pohar Perme, Stare, and
    Esteve (2012) <doi:10.1111/j.1541-0420.2011.01640.x>) estimators), and
    standardized incidence and mortality ratios, all of which can be
    easily adjusted for by covariates such as age. Fast splitting and
    aggregation of 'Lexis' objects (from package 'Epi') and other
    computations achieved using 'data.table'.
	"""
	
	homepage = "https://github.com/FinnishCancerRegistry/popEpi"
	cran = "popEpi" 

	version("0.4.11", md5="79f7118d4d398a4d75fddd8681ae42a5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-epi@2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
