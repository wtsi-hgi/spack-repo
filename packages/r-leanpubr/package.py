# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeanpubr(RPackage):
	"""'Leanpub' API Interface

	Provides access to the 'Leanpub' API
    <https://leanpub.com/help/api> for gathering information about 
    publications and submissions to the 'Leanpub' platform.
	"""
	
	homepage = "https://github.com/muschellij2/leanpubr"
	cran = "leanpubr" 

	version("0.3.1", md5="81497f13b21d70eece39a1dac2adc336")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
