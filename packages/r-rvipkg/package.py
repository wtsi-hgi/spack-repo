# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvipkg(RPackage):
	"""Regional Vulnerability Index

	The Regional Vulnerability Index (RVI), a statistical measure of brain structural abnormality, quantifies an individual's similarity to the expected pattern (effect size) of deficits in schizophrenia (Kochunov P, Fan F, Ryan MC, et al. (2020) <doi:10.1002/hbm.25045>).
	"""
	
	cran = "RVIpkg" 

	version("0.3.2", md5="322b9247ff155194882d26519cae3b02")

	depends_on("r@2.10:", type=("build", "run"))
