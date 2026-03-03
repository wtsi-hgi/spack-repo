# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExampadata(RPackage):
	"""Data Sets for Predictive Analytics Exam

	Contains all data sets for Exam PA: Predictive Analytics at 
    <https://exampa.net/>.
	"""
	
	homepage = "https://github.com/sdcastillo/ExamPAData"
	cran = "ExamPAData" 

	version("0.5.0", md5="28b4bd925b06a3b846351d6d5fa5cc6e")

	depends_on("r@3.5:", type=("build", "run"))
