# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdm(RPackage):
	"""Species Distribution Modelling

	An extensible framework for developing species distribution
    models using individual and community-based approaches, generate ensembles of
    models, evaluate the models, and predict species potential distributions in
    space and time. For more information, please check the following paper:
    Naimi, B., Araujo, M.B. (2016) <doi:10.1111/ecog.01881>.
	"""
	
	homepage = "https://www.biogeoinformatics.org"
	cran = "sdm" 

	version("1.1-8", md5="e92330823e733078c52253445b4ab9c3")

	depends_on("r-sp", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
