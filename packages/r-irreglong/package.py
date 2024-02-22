# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrreglong(RPackage):
	"""Analysis of Longitudinal Data with Irregular Observation Times

	Functions to help with analysis of longitudinal data featuring irregular observation times, where the observation times may be associated with the outcome process. There are functions to quantify the degree of irregularity, fit inverse-intensity weighted Generalized Estimating Equations (Lin H, Scharfstein DO, Rosenheck RA (2004) <doi:10.1111/j.1467-9868.2004.b5543.x>), perform multiple outputation (Pullenayegum EM (2016) <doi:10.1002/sim.6829>) and fit semi-parametric joint models (Liang Y (2009) <doi: 10.1111/j.1541-0420.2008.01104.x>).
	"""
	
	homepage = "https://epullenayegum.github.io/IrregLong/"
	cran = "IrregLong" 

	version("0.3.4", md5="99e64541087d5630f2b192089a7dc623")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
