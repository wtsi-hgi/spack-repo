# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisprose(RPackage):
	"""Discriminating Probes Selection

	Set of tools for molecular probes selection and design of a microarray, e.g. the assessment of physical and chemical properties, blast performance, selection according to sensitivity and selectivity. Methods used in package are described in: Lorenz R., Stephan H.B., Höner zu Siederdissen C. et al. (2011) <doi:10.1186/1748-7188-6-26>; Camacho C., Coulouris G., Avagyan V. et al. (2009) <doi:10.1186/1471-2105-10-421>.
	"""
	
	cran = "disprose" 

	version("0.1.6", md5="a27a49b35d530850cac8d684df29f390")

	depends_on("r@3.5:", type=("build", "run"))
