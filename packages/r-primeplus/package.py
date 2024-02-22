# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimeplus(RPackage):
	"""Study Design for Immunotherapy Clinical Trials

	Perform sample size, power calculation and subsequent analysis for Immuno-oncology (IO) trials composed of responders and non-responders.
	"""
	
	cran = "PRIMEplus" 

	version("1.0.16", md5="76f16861f1c7437447e25616260bb4b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
