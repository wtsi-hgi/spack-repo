# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinpk(RPackage):
	"""Generate Concentration-Time Profiles from Linear PK Systems

	Generate concentration-time profiles from linear pharmacokinetic
  (PK) systems, possibly with first-order absorption or zero-order infusion,
  possibly with one or more peripheral compartments, and possibly under
  steady-state conditions. Single or multiple doses may be specified. Secondary
  (derived) PK parameters (e.g. Cmax, Ctrough, AUC, Tmax, half-life, etc.) are
  computed.
	"""
	
	homepage = "https://github.com/benjaminrich/linpk"
	cran = "linpk" 

	version("1.1.2", md5="d5bc5dac5638f2eb4d4d86887285d191")

	depends_on("r-mvtnorm", type=("build", "run"))
