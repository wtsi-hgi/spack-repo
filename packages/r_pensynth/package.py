# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPensynth(RPackage):
	"""Penalized Synthetic Control Estimation

	Estimate penalized synthetic control models
    and perform hold-out validation to determine their 
    penalty parameter. This method is based on the work by
    Abadie & L'Hour (2021) <doi:10.1080/01621459.2021.1971535>.
    Penalized synthetic controls smoothly interpolate between 
    one-to-one matching and the synthetic control method.
	"""
	
	homepage = "https://github.com/vankesteren/pensynth"
	cran = "pensynth" 

	version("0.5.1", md5="9ee2502903067f53d8f9cefddaf203f9")

	depends_on("r-clarabel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
