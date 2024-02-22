# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetarange(RPackage):
	"""Framework to Build Mechanistic and Metabolic Constrained Species
Distribution Models

	Build spatially and temporally explicit
    process-based species distribution models, that can include an arbitrary
    number of environmental factors, species and processes including metabolic
    constraints and species interactions. The focus of the package is simulating
    populations of one or multiple species in a grid-based landscape and studying
    the meta-population dynamics and emergent patterns that arise from the
    interaction of species under complex environmental conditions. It
    provides functions for common ecological processes such as
    negative exponential, kernel-based dispersal (see
    Nathan et al. (2012) <doi:10.1093/acprof:oso/9780199608898.003.0015>),
    calculation of the environmental suitability based on cardinal values (
    Yin et al. (1995) <doi:10.1016/0168-1923(95)02236-Q>, simplified by
    Yan and Hunt (1999) <doi:10.1006/anbo.1999.0955> see eq: 4), reproduction in
    form of an Ricker model (see Ricker (1954) <doi:10.1139/f54-039> and
    Cabral and Schurr (2010) <doi:10.1111/j.1466-8238.2009.00492.x>),
    as well as metabolic scaling based on the metabolic theory of ecology
    (see Brown et al. (2004) <doi:10.1890/03-9000> and
    Brown, Sibly and Kodric-Brown (2012)
    <doi:10.1002/9781119968535.ch>).
	"""
	
	homepage = "https://metaRange.github.io/metaRange/"
	cran = "metaRange" 

	version("1.1.4", md5="cfbb2f567de76d5b1fed02db76ce2503")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
