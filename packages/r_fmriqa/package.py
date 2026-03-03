# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmriqa(RPackage):
	"""Functional MRI Quality Assurance Routines

	Methods for performing fMRI quality assurance (QA) measurements of
  test objects. Heavily  based on the fBIRN procedures detailed by Friedman and 
  Glover (2006) <doi:10.1002/jmri.20583>.
	"""
	
	cran = "fmriqa" 

	version("0.3.0", md5="10fd1c672a756d1e7b205890e6d083f3")

	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-optparse", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
