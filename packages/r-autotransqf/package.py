# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutotransqf(RPackage):
	"""A Novel Automatic Shifted Log Transformation

	A novel parametrization of log transformation and a shift parameter to automate the transformation process are proposed in R package 'AutoTransQF' based on Feng et al. (2016). Please read Feng et al. (2016) <doi:10.1002/sta4.104> for more details of the method.
	"""
	
	homepage = "https://github.com/yyyuehhu/AutoTransQF"
	cran = "AutoTransQF" 

	version("0.1.3", md5="4240adbd6e6c4035ec30255b070776fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-matlab2r", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
