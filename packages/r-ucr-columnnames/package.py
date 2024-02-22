# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcrColumnnames(RPackage):
	"""Fixes Column Names for Uniform Crime Report "Offenses Known and
Clearance by Arrest" Datasets

	Changes the column names of the inputted dataset to the correct
    names from the Uniform Crime Report codebook for the "Offenses Known and
    Clearance by Arrest" datasets from 1998-2014.
	"""
	
	cran = "UCR.ColumnNames" 

	version("0.1.0", md5="f44a47a034bdb45f7584bde3962ea804")

	depends_on("r@2.10:", type=("build", "run"))
