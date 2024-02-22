# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimr(RPackage):
	"""Power Analysis for Generalised Linear Mixed Models by Simulation

	Calculate power for generalised linear mixed models, using
    simulation. Designed to work with models fit using the 'lme4' package.
    Described in Green and MacLeod, 2016 <doi:10.1111/2041-210X.12504>.
	"""
	
	homepage = "https://github.com/pitakakariki/simr"
	cran = "simr" 

	version("1.0.7", md5="12b6d4cca32535d362ebd9e600b8acb9")

	depends_on("r-lme4@1.1.16:", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-pbkrtest", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlrsim", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lmertest@3.0.0:", type=("build", "run"))
