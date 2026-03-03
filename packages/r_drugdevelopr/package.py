# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugdevelopr(RPackage):
	"""Utility-Based Optimal Phase II/III Drug Development Planning

	Plan optimal sample size allocation and go/no-go decision rules
  for phase II/III drug development programs with time-to-event, binary or
  normally distributed endpoints when assuming fixed treatment effects or a
  prior distribution for the treatment effect, using methods from Kirchner et al.
  (2016) <doi:10.1002/sim.6624> and Preussler (2020). Optimal is in the sense of
  maximal expected utility, where the utility is a function taking into account
  the expected cost and benefit of the program. It is possible to extend to more
  complex settings with bias correction (Preussler S et al. (2020)
  <doi:10.1186/s12874-020-01093-w>),  multiple phase III trials (Preussler et
  al. (2019) <doi:10.1002/bimj.201700241>), multi-arm trials (Preussler et al.
  (2019) <doi:10.1080/19466315.2019.1702092>), and multiple endpoints
  (Kieser et al. (2018) <doi:10.1002/pst.1861>).
	"""
	
	homepage = "https://github.com/Sterniii3/drugdevelopR"
	cran = "drugdevelopR" 

	version("1.0.1", md5="01fdcdfa92ca3b70668f651c44a26ba8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
