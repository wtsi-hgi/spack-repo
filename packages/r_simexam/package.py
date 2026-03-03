# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimexam(RPackage):
	"""Generate Simulated Data for IRT-Enabled Exams

	Generates binary test data based on Item Response Theory using the two-parameter logistic model (Lord, 1980 <doi:10.4324/9780203056615>). Useful functions for test equating are included, e.g. functions for generating internal and external common items between test forms and a function to create a linkage plans between those forms. Ancillary functions for generating true item and person parameters as well as for calculating the probability of a person correctly answering an item are also included.
	"""
	
	cran = "simExam" 

	version("1.0.0", md5="079e3f4041bf3307c231237c283ba2d2")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
