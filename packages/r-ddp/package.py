# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdp(RPackage):
	"""Desirable Dietary Pattern

	The desirable Dietary Pattern (DDP)/ PPH score
  measures the variety of food consumption. The (weighted) score is calculated 
  based on the type of food. This package is intended to calculate
  the DDP/ PPH score that is faster than traditional method via 
  a manual calculation by BKP (2017) <http://bkp.pertanian.go.id/storage/app/uploads/public/5bf/ca9/06b/5bfca906bc654274163456.pdf> and is simpler than the nutrition survey 
  <http://www.nutrisurvey.de>. The database to create weights and baseline values
  is the Indonesia national survey in 2017.
	"""
	
	cran = "ddp" 

	version("0.0.3", md5="f0a598bd68f07c54a320ec4a5c9d1f43")

	depends_on("r@2.10:", type=("build", "run"))
