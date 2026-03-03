# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtmm(RPackage):
	"""Continuous-Time Movement Modeling

	Functions for identifying, fitting, and applying continuous-space, continuous-time stochastic-process movement models to animal tracking data.
  The package is described in Calabrese et al (2016) <doi:10.1111/2041-210X.12559>, with models and methods based on those introduced and detailed in
  Fleming & Calabrese et al (2014) <doi:10.1086/675504>,
  Fleming et al (2014) <doi:10.1111/2041-210X.12176>,
  Fleming et al (2015) <doi:10.1103/PhysRevE.91.032107>,
  Fleming et al (2015) <doi:10.1890/14-2010.1>,
  Fleming et al (2016) <doi:10.1890/15-1607>,
  Péron & Fleming et al (2016) <doi:10.1186/s40462-016-0084-7>,
  Fleming & Calabrese (2017) <doi:10.1111/2041-210X.12673>,
  Péron et al (2017) <doi:10.1002/ecm.1260>,
  Fleming et al (2017) <doi:10.1016/j.ecoinf.2017.04.008>,
  Fleming et al (2018) <doi:10.1002/eap.1704>,
  Winner & Noonan et al (2018) <doi:10.1111/2041-210X.13027>,
  Fleming et al (2019) <doi:10.1111/2041-210X.13270>,
  Noonan & Fleming et al (2019) <doi:10.1186/s40462-019-0177-1>,
  Fleming et al (2020) <doi:10.1101/2020.06.12.130195>,
  Noonan et al (2021) <doi:10.1111/2041-210X.13597>,
  Fleming et al (2022) <doi:10.1111/2041-210X.13815>,
  Silva et al (2022) <doi:10.1111/2041-210X.13786>,
  Alston & Fleming et al (2023) <doi:10.1111/2041-210X.14025>.
	"""
	
	homepage = "https://github.com/ctmm-initiative/ctmm"
	cran = "ctmm" 

	version("1.2.0", md5="2490232efcb2bf6e2828c1e1290c2118")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bessel", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-fasttime", type=("build", "run"))
	depends_on("r-gmedian", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-manipulate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
