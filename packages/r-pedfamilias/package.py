# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedfamilias(RPackage):
	"""Import and Export 'Familias' Files

	Tools for exchanging pedigree data between the 'pedsuite'
    packages and the 'Familias' software for forensic kinship computations
    (Egeland et al. (2000) <doi:10.1016/s0379-0738(00)00147-x>). These
    functions were split out from the 'forrel' package to streamline
    maintenance and provide a lightweight alternative for packages otherwise
    independent of 'forrel'.
	"""
	
	homepage = "https://github.com/magnusdv/pedFamilias"
	cran = "pedFamilias" 

	version("0.2.0", md5="df58ae11a093224a88690858d5ebd313")

	depends_on("r-pedtools", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-pedmut", type=("build", "run"))
