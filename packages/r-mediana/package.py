# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMediana(RPackage):
	"""Clinical Trial Simulations

	Provides a general framework for clinical trial simulations based
    on the Clinical Scenario Evaluation (CSE) approach. The package supports a
    broad class of data models (including clinical trials with continuous, binary,
    survival-type and count-type endpoints as well as multivariate outcomes that are
    based on combinations of different endpoints), analysis strategies and commonly
    used evaluation criteria.
	"""
	
	homepage = "http://gpaux.github.io/Mediana/"
	cran = "Mediana" 

	version("1.0.8", md5="3d874918b4e0b959078d3e71ba417b8a")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
