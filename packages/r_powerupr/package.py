# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerupr(RPackage):
	"""Power Analysis Tools for Multilevel Randomized Experiments

	
 Includes tools to calculate statistical power, minimum detectable effect size (MDES), MDES difference (MDESD), and minimum required sample size for various multilevel randomized experiments (MRE) with continuous outcomes.
 Accomodates 14 types of MRE designs to detect main treatment effect, seven types of MRE designs to detect moderated treatment effect (2-1-1, 2-1-2, 2-2-1, 2-2-2, 3-3-1, 3-3-2, and 3-3-3 designs; <total.lev> - <trt.lev> - <mod.lev>),
 five types of MRE designs to detect mediated treatment effects (2-1-1, 2-2-1, 3-1-1, 3-2-1, and 3-3-1 designs; <trt.lev> - <med.lev> - <out.lev>), four types of partially nested (PN) design to detect main treatment effect,
 and three types of PN designs to detect mediated treatment effects (2/1, 3/1, 3/2; <trt.arm.lev> / <ctrl.arm.lev>). 
 See 'PowerUp!' Excel series at <https://www.causalevaluation.org/>. 
	"""
	
	cran = "PowerUpR" 

	version("1.1.0", md5="f329384c32cee3d4e744cb1f60efd8fb")

