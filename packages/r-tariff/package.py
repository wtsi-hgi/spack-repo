# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTariff(RPackage):
	"""Replicate Tariff Method for Verbal Autopsy

	Implement the Tariff algorithm for coding cause-of-death from verbal autopsies. The Tariff method was originally proposed in James et al (2011) <DOI:10.1186/1478-7954-9-31> and later refined as Tariff 2.0 in Serina, et al. (2015) <DOI:10.1186/s12916-015-0527-9>. Note that this package was not developed by authors affiliated with the Institute for Health Metrics and Evaluation and thus unintentional discrepancies may exist between the this implementation and the implementation available from IHME.
	"""
	
	cran = "Tariff" 

	version("1.0.5", md5="161c1466d1cc217a70ecb46d6b4e076a")

