# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVol2birdr(RPackage):
	"""Vertical Profiles of Biological Signals in Weather Radar Data

	'R' implementation of the 'vol2bird' software for generating vertical profiles
    of birds and other biological signals in weather radar data. See Dokter et al.
    (2011) <doi:10.1098/rsif.2010.0116> for a paper describing the methodology.
	"""
	
	homepage = "https://github.com/adokter/vol2birdR/"
	cran = "vol2birdR" 

	version("1.0.2", md5="67efb44b6a7b8311c7845953551175f6")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-pkgbuild", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
	depends_on("hdf5", type=("build", "link", "run"))
	depends_on("proj", type=("build", "link", "run"))
