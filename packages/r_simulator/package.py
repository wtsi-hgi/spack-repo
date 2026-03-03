# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimulator(RPackage):
	"""An Engine for Running Simulations

	A framework for performing simulations such as those common in
    methodological statistics papers.  The design principles of this package
    are described in greater depth in Bien, J. (2016) "The simulator: An Engine
    to Streamline Simulations," which is available at <arXiv:1607.00021>.
	"""
	
	homepage = "https://github.com/jacobbien/simulator"
	cran = "simulator" 

	version("0.2.5", md5="61013b9c35dfc56cc65e640c7ee86910")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
