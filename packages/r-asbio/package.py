# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsbio(RPackage):
	"""A Collection of Statistical Tools for Biologists

	Contains functions from: Aho, K. (2014) Foundational and Applied Statistics for Biologists using R.  CRC/Taylor and Francis, Boca Raton, FL, ISBN: 978-1-4398-7338-0.
	"""
	
	cran = "asbio" 

	version("1.9-7", md5="eb113cbc977a02bbaa2e06e4560dd65b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-pixmap", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-gwidgets2", type=("build", "run"))
	depends_on("r-gwidgets2tcltk", type=("build", "run"))
