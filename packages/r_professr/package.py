# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfessr(RPackage):
	"""Grades Setting and Exam Maker

	Programs to determine student grades and create
  examinations from Question banks.  Programs will create numerous
  multiple choice exams, randomly shuffled, for different versions of same question list.
	"""
	
	cran = "ProfessR" 

	version("2.4-3", md5="86ca6a55c55498305c75ca408b6659dd")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-rpmg", type=("build", "run"))
