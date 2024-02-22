# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFqadata(RPackage):
	"""Contains Regional Floristic Quality Assessment Databases

	Contains regional Floristic Quality Assessment databases that
    have been approved or approved with reservations by the U.S. Army
    Corps of Engineers (USACE). Paired with the 'fqacalc' R package, these
    data sets allow for Floristic Quality Assessment metrics to be
    calculated. For information on FQA see Spyreas (2019)
    <doi:10.1002/ecs2.2825>. Both packages were developed for the USACE by
    the U.S.  Army Engineer Research and Development Center's
    Environmental Laboratory.
	"""
	
	cran = "fqadata" 

	version("1.1.0", md5="912ac6c0118ad0175e0ef37a56f751b0")

	depends_on("r@2.10:", type=("build", "run"))
