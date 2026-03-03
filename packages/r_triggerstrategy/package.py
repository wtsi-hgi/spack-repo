# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriggerstrategy(RPackage):
	"""Trigger Strategy in Clinical Trials

	The trigger strategy is a general framework for a multistage statistical design with multiple hypotheses, allowing an adaptive selection of interim analyses. The selection of interim stages can be associated with some prespecified endpoints which serve as the trigger. This selection allows us to refine the critical boundaries in hypotheses testing procedures, and potentially increase the statistical power. This package includes several trial designs using the trigger strategy. 
    See Gou, J. (2023), "Trigger strategy in repeated tests on multiple hypotheses", Statistics in Biopharmaceutical Research, 15(1), 133-140, and Gou, J. (2022), "Sample size optimization and initial allocation of the significance levels in group sequential trials with multiple endpoints", Biometrical Journal, 64(2), 301-311.
	"""
	
	cran = "triggerstrategy" 

	version("1.2.0", md5="3a83a5e195a97ceac1c561d75597e4f6")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ga@3:", type=("build", "run"))
	depends_on("r-ldbounds@2:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1:", type=("build", "run"))
	depends_on("r-nleqslv@3:", type=("build", "run"))
