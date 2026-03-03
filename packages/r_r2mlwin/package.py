# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2mlwin(RPackage):
	"""Running 'MLwiN' from Within R

	An R command interface to the 'MLwiN' multilevel
    modelling software package.
	"""
	
	homepage = "http://www.bristol.ac.uk/cmm/software/r2mlwin/"
	cran = "R2MLwiN" 

	version("0.8-9", md5="f5467eeaa1ffba61634f71f194a77c54")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreign@0.8.46:", type=("build", "run"))
	depends_on("r-r2winbugs", type=("build", "run"))
	depends_on("r-digest@0.6.5:", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-coda@0.16.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-memisc", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
