# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLibrarian(RPackage):
	"""Install, Update, Load Packages from CRAN, 'GitHub', and
'Bioconductor' in One Step

	Automatically install, update, and load 'CRAN', 'GitHub', and 'Bioconductor' 
    packages in a single function call. By accepting bare unquoted names for packages, 
    it's easy to add or remove packages from the list.
	"""
	
	homepage = "https://github.com/DesiQuintans/librarian"
	cran = "librarian" 

	version("1.8.1", md5="84c9b5f1aa24897e73802c1975533c51")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
