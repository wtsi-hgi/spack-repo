# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMigconnectivity(RPackage):
	"""Estimate Migratory Connectivity for Migratory Animals

	Allows the user to estimate transition probabilities for
    migratory animals between any two phases of the annual cycle, using a
    variety of different data types. Also quantifies the strength of
    migratory connectivity (MC), a standardized metric to quantify the
    extent to which populations co-occur between two phases of the annual
    cycle. Includes functions to estimate MC and the more traditional
    metric of migratory connectivity strength (Mantel correlation)
    incorporating uncertainty from multiple sources of sampling error. For
    cross-species comparisons, methods are provided to estimate
    differences in migratory connectivity strength, incorporating
    uncertainty. See Cohen et al. (2018) <doi:10.1111/2041-210X.12916>,
    Cohen et al. (2019) <doi:10.1111/ecog.03974>, and Roberts et al.
    (2023) <doi:10.1002/eap.2788> for details on some of these methods.
	"""
	
	homepage = "https://github.com/SMBC-NZP/MigConnectivity"
	cran = "MigConnectivity" 

	version("0.4.7", md5="b7f4c7733cd9213d4ef12e82fc12e4e2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ncf", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-rmark@2.1.14:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
