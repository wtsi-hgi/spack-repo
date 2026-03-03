# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNovicedeveloperresources2(RPackage):
	"""Further Resources to Assist Novice Developers

	Assist novice developers when preparing a single package or a set of integrated packages to submit to CRAN. Provide additional resources to facilitate the automation of the following individual or batch processing: check local source packages;  build local .tar.gz source files; install packages from local .tar.gz files; detect conflicts between function names in the environment. The additional resources include determining the identity and ordering of the packages to process when updating an imported package.
	"""
	
	cran = "NoviceDeveloperResources2" 

	version("1.0", md5="71f99b255dabf0926c44f8f5361c9248", url="https://cran.r-project.org/src/contrib/NoviceDeveloperResources2_1.0.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-packrat", type=("build", "run"))
	depends_on("r-novicedeveloperresources", type=("build", "run"))
