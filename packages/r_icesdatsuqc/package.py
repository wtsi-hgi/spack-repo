# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcesdatsuqc(RPackage):
	"""Run Quality Checks on Data Prior to Submission to ICES

	Run quality checks on data sets using the same checks that are conducted
  on the ICES Data Submission Utility (DATSU) <https://datsu.ices.dk/web/index.aspx>.
	"""
	
	homepage = "https://datsu.ices.dk/web/index.aspx"
	cran = "icesDatsuQC" 

	version("1.0.1", md5="1667f2ff0dfa0dc70de3f9aafae19030")

	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-icesdatsu@1.1:", type=("build", "run"))
