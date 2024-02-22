# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROc(RPackage):
	"""Optimal Classification Roll Call Analysis Software

	Estimates optimal classification (Poole 2000) <doi:10.1093/oxfordjournals.pan.a029814>
		scores from roll call votes supplied though a 'rollcall'
		object from package 'pscl'.
	"""
	
	homepage = "https://legacy.voteview.com/oc_in_R.htm"
	cran = "oc" 

	version("1.2.1", md5="0bb2b6822f3f590c757b0461ac90561b")

	depends_on("r@2.3.1:", type=("build", "run"))
	depends_on("r-pscl@0.59:", type=("build", "run"))
