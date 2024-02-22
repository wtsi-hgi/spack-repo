# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRyoutheria(RPackage):
	"""Access to the YouTheria Mammal Trait Database

	A programmatic interface to web-services of YouTheria. YouTheria is
    an online database of mammalian trait data <http://www.utheria.org/>.
	"""
	
	homepage = "https://github.com/BiologicalRecordsCentre/rYoutheria"
	cran = "rYoutheria" 

	version("1.0.3", md5="a1bc0e30ec9bf39c86b9745cbade6a4c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
