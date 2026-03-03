# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoedata(RPackage):
	"""Data Sets from "Lectures on Econometrics" by Chirok Han

	Data sets for Chirok Han (2022, ISBN:979-11-303-1497-6,
  "Lectures on Econometrics"). Students, teachers, and self-learners will
  find the data sets essential for replicating the results in the book.
	"""
	
	cran = "loedata" 

	version("1.0.1", md5="de036adca6086869f118521af47067de")

	depends_on("r@3:", type=("build", "run"))
