# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlpreemption(RPackage):
	"""Maximum Likelihood Estimation of the Niche Preemption Model

	Provides functions for obtaining estimates of the parameter of the niche preemption model (also known as the geometric series), in particular a maximum likelihood estimator (Graffelman, 2021) <doi:10.1101/2021.01.27.428381>. The niche preemption model is a widely used model in ecology and biodiversity studies.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "MLpreemption" 

	version("1.0.1", md5="c0d73c9c7cfa6ddf606bab5eef0c066e")

	depends_on("r@1.8:", type=("build", "run"))
