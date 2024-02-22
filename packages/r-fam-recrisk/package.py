# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamRecrisk(RPackage):
	"""Familial Recurrence Risk

	Given vectors of family sizes and number of affecteds per family, calculates the risk of disease recurrence in an unaffected person, conditional on a family having at least k affected members. Methods also model heterogeneity of disease risk across families by fitting a mixture model, allowing for high and low risk families.
	"""
	
	cran = "fam.recrisk" 

	version("0.1", md5="7e4108c356ea23b1db1603176dd5c588")

	depends_on("r@3.2:", type=("build", "run"))
