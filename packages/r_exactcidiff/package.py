# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactcidiff(RPackage):
	"""Inductive Confidence Intervals for the Difference Between Two
Proportions

	This is a package for exact Confidence Intervals for the difference between two independent or dependent proportions.
	"""
	
	homepage = "https://urldefense.proofpoint.com/v2/url?u=http-3A__www.R-2Dproject.org&d=DwICaQ&c=sJ6xIWYx-zLMB3EPkvcnVg&r=u5749-0kOlGR1AfizUVmaw&m=qjJHLdipM5gUyXllZWH5kL0wENGFef6KuJ57hW5lHx14eZasfdmgFN_1geUbxk5J&s=VFf9h_9FOlJBpRMIjim8tGuVnJ7GlWc5qZkrA9kmoMM&e="
	cran = "ExactCIdiff" 

	version("2.1", md5="c94b41b0056dc90a04a7ccd1724c941f")

	depends_on("r@1.8:", type=("build", "run"))
