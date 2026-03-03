# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGxescanr(RPackage):
	"""Run GWAS/GWEIS Scans Using Binary Dosage Files

	Tools to run genome-wide association study (GWAS) and
  genome-wide by environment interaction study (GWEIS) scans using the genetic
  data stored in a binary dosage file. The user provides a data frame with
  the subject's covariate data and the information about the binary dosage
  file returned by the BinaryDosage::getbdinfo() routine.
	"""
	
	cran = "GxEScanR" 

	version("2.0.2", md5="4322771b968e46d4b2866e284b9da4a9")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
