# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaptr(RPackage):
	"""Representative and Adequate Prioritization Toolkit in R

	Biodiversity is in crisis. The overarching aim of conservation
    is to preserve biodiversity patterns and processes. To this end, protected
    areas are established to buffer species and preserve biodiversity processes.
    But resources are limited and so protected areas must be cost-effective.
    This package contains tools to generate plans for protected areas
    (prioritizations), using spatially explicit targets for biodiversity
    patterns and processes. To obtain solutions in a feasible amount  of time,
    this package uses the commercial 'Gurobi' software (obtained from
    <https://www.gurobi.com/>). For more information on using
    this package, see Hanson et al. (2018) <doi:10.1111/2041-210X.12862>.
	"""
	
	homepage = "https://jeffrey-hanson.com/raptr/"
	cran = "raptr" 

	version("1.0.1", md5="78931395e4e167e95959bc0a3658f8c5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sf@1.0.9:", type=("build", "run"))
	depends_on("r-terra@1.6.47:", type=("build", "run"))
	depends_on("r-sp@1.4.6:", type=("build", "run"))
	depends_on("r-matrix@1.4.1:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-boot@1.3.28:", type=("build", "run"))
	depends_on("r-pbsmapping@2.73:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-shape@1.4.6:", type=("build", "run"))
	depends_on("r-adehabitathr@0.4.19:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-hypervolume@2.0.7:", type=("build", "run"))
	depends_on("r-ks@1.13.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.3:", type=("build", "run"))
	depends_on("r-withr@2.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
