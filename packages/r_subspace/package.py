# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubspace(RPackage):
	"""Interface to OpenSubspace

	An interface to 'OpenSubspace', an open source framework for
  evaluation and exploration of subspace clustering algorithms in WEKA 
  (see <http://dme.rwth-aachen.de/de/opensubspace> for more
  information).  Also performs visualization.
	"""
	
	cran = "subspace" 

	version("1.0.4", md5="3f3115eb8e6acaf508d318bd109a1f45")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggvis@0.4.2:", type=("build", "run"))
	depends_on("r-colorspace@1:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-rjava@0.9:", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
