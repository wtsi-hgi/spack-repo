# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlorabr(RPackage):
	"""Explore Brazilian Flora 2020 Database

	A collection of functions designed to retrieve, filter and spatialize data from the Brazilian Flora 2020 dataset. For more information about the dataset, please visit <https://floradobrasil.jbrj.gov.br/consulta/>.
	"""
	
	homepage = "https://wevertonbio.github.io/florabr/"
	cran = "florabr" 

	version("1.1.0", md5="abf90a5ad8222dbdf87d38cc94cdd916")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xml@3.99.0.14:", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-httr@1.4.6:", type=("build", "run"))
	depends_on("r-terra@1.7.39:", type=("build", "run"))
