# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrcov3way(RPackage):
	"""Robust Methods for Multiway Data Analysis, Applicable also for
Compositional Data

	Provides methods for multiway data analysis by means of Parafac
    and Tucker 3 models. Robust versions (Engelen and Hubert (2011) <doi:10.1016/j.aca.2011.04.043>) and versions
    for compositional data are also provided (Gallo (2015) <doi:10.1080/03610926.2013.798664>, Di Palma et al. (2018) <doi:10.1080/02664763.2017.1381669>).
    Several optimization methods alternative to ALS are available 
    (Simonacci and Gallo (2019) <doi:10.1016/j.chemolab.2019.103822>, Simonacci and Gallo (2020) <doi:10.1007/s00500-019-04320-9>).
	"""
	
	homepage = "https://github.com/valentint/rrcov3way"
	cran = "rrcov3way" 

	version("0.5-0", md5="923bfd474b461600cd57ece3834635aa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-threeway", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
