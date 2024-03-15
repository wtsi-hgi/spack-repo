# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccucor(RPackage):
	"""Natural Abundance Correction of Mass Spectrometer Data

	An isotope natural abundance correction algorithm that
  is needed especially for high resolution mass spectrometers. Supports
  correction for 13C, 2H and 15N. Su X, Lu W and Rabinowitz J (2017)
  <doi:10.1021/acs.analchem.7b00396>.
	"""
	
	homepage = "https://github.com/XiaoyangSu/AccuCor"
	cran = "accucor" 

	version("0.3.1", md5="dbbb5d9781f0f15d2f2418568b82bf24")

	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-chnosz", type=("build", "run"))
